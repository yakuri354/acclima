/**
 * NoiseModelling is an open-source tool designed to produce environmental noise maps on very large urban areas. It can be used as a Java library or be controlled through a user friendly web interface.
 *
 * This version is developed by Université Gustave Eiffel and CNRS
 * <http://noise-planet.org/noisemodelling.html>
 *
 * NoiseModelling is distributed under GPL 3 license. You can read a copy of this License in the file LICENCE provided with this software.
 *
 * Contact: contact@noise-planet.org
 **/
/**
 * @Author Valentin Le Bescond, Université Gustave Eiffel
 * @Author Nicolas Fortin, Université Gustave Eiffel
 * @Author Gwendall Petit, Cerema
 */

package com.acclima.backend2

import crosby.binary.osmosis.OsmosisReader
import groovy.sql.Sql
import org.h2gis.utilities.wrapper.ConnectionWrapper
import org.locationtech.jts.geom.Geometry
import org.locationtech.jts.geom.GeometryFactory
import org.openstreetmap.osmosis.core.container.v0_6.EntityContainer
import org.openstreetmap.osmosis.core.container.v0_6.NodeContainer
import org.openstreetmap.osmosis.core.container.v0_6.RelationContainer
import org.openstreetmap.osmosis.core.container.v0_6.WayContainer
import org.openstreetmap.osmosis.core.domain.v0_6.*
import org.openstreetmap.osmosis.core.task.v0_6.RunnableSource
import org.openstreetmap.osmosis.core.task.v0_6.Sink
import org.openstreetmap.osmosis.xml.common.CompressionMethod
import org.openstreetmap.osmosis.xml.v0_6.XmlReader
import org.slf4j.Logger
import org.slf4j.LoggerFactory

import java.sql.Connection

// main function of the script
def loadOSMData(RunnableSource reader, Sql sql, String tableName = "MAP_BUILDINGS_GEOM") {
    def srid = 3857 // TODO

    Logger logger = LoggerFactory.getLogger("com.acclima.backend2")
    logger.info('Start : Get Buildings from OSM')
    logger.info("inputs {}", )

    OsmHandler handler = new OsmHandler(logger, false, false, false, false)
    reader.setSink(handler)
    reader.run()

    logger.info('OSM Read done')

    sql.execute("DROP TABLE IF EXISTS ?", [tableName])
    sql.execute("""CREATE TABLE ? ( 
        ID_WAY integer PRIMARY KEY, 
        THE_GEOM geometry,
        HEIGHT real
    );""", [tableName])

    for (Building building : handler.buildings) {
        // sql.execute("INSERT INTO " + tableName + " VALUES (" + building.id + ", ST_MakeValid(ST_SIMPLIFYPRESERVETOPOLOGY(ST_Transform(ST_GeomFromText('" + building.geom + "', 4326), " + srid + "),0.1)), " + building.height + ")")
        sql.execute("INSERT INTO ? VALUES (?, ST_MakeValid(ST_SIMPLIFYPRESERVETOPOLOGY(ST_Transform(ST_GeomFromText(?, 4326), ?),0.1)), ?)", [tableName, building.id, building.geom, srid, building.height])
    }

    sql.execute("""
        CREATE SPATIAL INDEX IF NOT EXISTS BUILDINGS_INDEX ON ? (the_geom);
        -- List buildings that intersects with other buildings that have a greater area
        DROP TABLE IF EXISTS tmp_relation_buildings_buildings;
        CREATE TABLE tmp_relation_buildings_buildings AS SELECT s1.ID_WAY as PK_BUILDING, S2.ID_WAY as PK2_BUILDING FROM MAP_BUILDINGS_GEOM S1, MAP_BUILDINGS_GEOM S2 WHERE ST_AREA(S1.THE_GEOM) < ST_AREA(S2.THE_GEOM) AND S1.THE_GEOM && S2.THE_GEOM AND ST_DISTANCE(S1.THE_GEOM, S2.THE_GEOM) <= 0.1;
        
        -- Alter that small area buildings by removing shared area
        DROP TABLE IF EXISTS tmp_buildings_truncated;
        CREATE TABLE tmp_buildings_truncated AS SELECT PK_BUILDING, ST_DIFFERENCE(s1.the_geom, ST_BUFFER(ST_Collect(s2.the_geom), 0.1, 'join=mitre')) the_geom, s1.HEIGHT HEIGHT from tmp_relation_buildings_buildings r, MAP_BUILDINGS_GEOM s1, MAP_BUILDINGS_GEOM s2 WHERE PK_BUILDING = S1.ID_WAY AND PK2_BUILDING = S2.ID_WAY  GROUP BY PK_BUILDING;
        
        -- Merge original buildings with altered buildings 
        DROP TABLE IF EXISTS BUILDINGS;
        CREATE TABLE BUILDINGS(PK INTEGER PRIMARY KEY, THE_GEOM GEOMETRY, HEIGHT real);
        SELECT s.id_way, ST_SETSRID(s.the_geom, ''' + srid + '''), s.HEIGHT into BUILDINGS from MAP_BUILDINGS_GEOM s where id_way not in (select PK_BUILDING from tmp_buildings_truncated) UNION ALL select PK_BUILDING, ST_SETSRID(the_geom, ''' + srid + '''), HEIGHT from tmp_buildings_truncated WHERE NOT st_isempty(the_geom);

        DROP TABLE IF EXISTS tmp_buildings_truncated;
        DROP TABLE IF EXISTS tmp_relation_buildings_buildings;
        DROP TABLE IF EXISTS MAP_BUILDINGS_GEOM;
    """, [tableName])

    sql.execute("CREATE SPATIAL INDEX IF NOT EXISTS BUILDING_GEOM_INDEX ON BUILDINGS(THE_GEOM)");

    sql.execute("DROP TABLE IF EXISTS ROADS")
    sql.execute("CREATE TABLE ROADS (PK serial PRIMARY KEY, ID_WAY integer, THE_GEOM geometry, TYPE varchar, LV_D integer, LV_E integer,LV_N integer,HV_D integer,HV_E integer,HV_N integer,LV_SPD_D integer,LV_SPD_E integer,LV_SPD_N integer,HV_SPD_D integer, HV_SPD_E integer,HV_SPD_N integer, PVMT varchar(10));")

    for (Road road : handler.roads) {
        if (road.geom.isEmpty()) {
            continue
        }
        String query = "INSERT INTO ROADS(ID_WAY, THE_GEOM, TYPE, LV_D, LV_E, LV_N, HV_D, HV_E, HV_N, LV_SPD_D, LV_SPD_E, LV_SPD_N, HV_SPD_D, HV_SPD_E, HV_SPD_N, PVMT) VALUES (?, st_setsrid(st_updatez(ST_precisionreducer(ST_SIMPLIFYPRESERVETOPOLOGY(ST_TRANSFORM(ST_GeomFromText(?, 4326), ?),0.1),1), 0.05), ?),?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
        sql.execute(query, [road.id, road.geom, srid, srid, road.type,
                            road.getNbLV("d"), road.getNbLV("e"), road.getNbLV("n"),
                            road.getNbHV("d"), road.getNbHV("e"), road.getNbHV("n"),
                            Road.speed[road.category], Road.speed[road.category], Road.speed[road.category],
                            Math.min(90, Road.speed[road.category]), Math.min(90, Road.speed[road.category]), Math.min(90, Road.speed[road.category]),
                            'NL08'])
    }
    sql.execute("CREATE SPATIAL INDEX IF NOT EXISTS ROADS_GEOM_INDEX ON " + "ROADS" + "(THE_GEOM)")

        sql.execute("DROP TABLE IF EXISTS GROUND")
        sql.execute("CREATE TABLE GROUND (PK serial PRIMARY KEY, ID_WAY int, THE_GEOM geometry, PRIORITY int, G double);")

    for (Ground ground : handler.grounds) {
        if (ground.priority == 0) {
            continue
        }
        if (ground.geom.isEmpty()) {
            continue
        }
        // sql.execute("INSERT INTO GROUND (ID_WAY, THE_GEOM, PRIORITY, G) VALUES (" + ground.id + ", ST_Transform(ST_GeomFromText('" + ground.geom + "', 4326), " + srid + "), " + ground.priority + ", " + ground.coeff_G + ")")
        sql.execute("INSERT INTO GROUND (ID_WAY, THE_GEOM, PRIORITY, G) VALUES (?, ST_Transform(ST_GeomFromText(?, 4326), ?), ?, ?)", [ground.id, ground.geom, srid, ground.priority, ground.coeff_G])
    }
    sql.execute("CREATE SPATIAL INDEX IF NOT EXISTS GROUND_GEOM_INDEX ON GROUND(THE_GEOM)")

    logger.info('SQL INSERT done')

    resultString = "nodes : " + handler.nb_nodes
    resultString += "<br>\n"
    resultString += "ways : " + handler.nb_ways
    resultString += "<br>\n"
    resultString += "relations : " + handler.nb_relations
    resultString += "<br>\n"
    resultString += "buildings : " + handler.nb_buildings
    resultString += "<br>\n"
    resultString += "roads : " + handler.nb_roads
    resultString += "<br>\n"
    resultString += "grounds : " + handler.nb_grounds
    resultString += "<br>\n"

    logger.info('End : Get Buildings from OSM')
    logger.info('Result : ' + resultString)
}

class OsmHandler implements Sink {

    public int nb_ways = 0
    public int nb_nodes = 0
    public int nb_relations = 0
    public int nb_buildings = 0
    public int nb_roads = 0
    public int nb_grounds = 0

    Random rand = new Random()

    public Map<Long, Node> nodes = new HashMap<Long, Node>()
    public Map<Long, Way> ways = new HashMap<Long, Way>()
    public Map<Long, Relation> relations = new HashMap<Long, Relation>()
    public List<Building> buildings = new ArrayList<Building>()
    public List<Road> roads = new ArrayList<Road>()
    public List<Ground> grounds = new ArrayList<Ground>()

    Logger logger
    boolean ignoreBuildings
    boolean ignoreRoads
    boolean ignoreGround
    boolean removeTunnels

    OsmHandler(Logger logger, boolean ignoreBuildings, boolean ignoreRoads, boolean ignoreGround, boolean removeTunnels) {
        this.logger = logger
        this.ignoreBuildings = ignoreBuildings
        this.ignoreRoads = ignoreRoads
        this.ignoreGround = ignoreGround
        this.removeTunnels = removeTunnels
    }

    @Override
    void initialize(Map<String, Object> arg0) {}

    @Override
    void process(EntityContainer entityContainer) {
        if (entityContainer instanceof NodeContainer) {
            nb_nodes++
            Node node = ((NodeContainer) entityContainer).getEntity()
            nodes.put(node.getId(), node)
        } else if (entityContainer instanceof WayContainer) {
            nb_ways++
            Way way = ((WayContainer) entityContainer).getEntity()
            ways.put(way.getId(), way)
            boolean isBuilding = false
            boolean isRoad = false
            boolean isTunnel = false
            double height = 4.0 + rand.nextDouble() * 2.1
            boolean trueHeightFound = false
            for (Tag tag : way.getTags()) {
                if ("building".equalsIgnoreCase(tag.getKey())) {
                    isBuilding = true
                }
                if ("tunnel".equalsIgnoreCase(tag.getKey()) && "yes".equalsIgnoreCase(tag.getValue())) {
                    isTunnel = true
                }
                if ("highway".equalsIgnoreCase((tag.getKey()))) {
                    isRoad = true
                }
                if (isBuilding) {
                    if (!trueHeightFound && "building:levels".equalsIgnoreCase(tag.getKey())) {
                        height = height - 4 + Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", "")) * 3.0
                    }
                    if ("height".equalsIgnoreCase(tag.getKey())) {
                        height = Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", ""))
                        trueHeightFound = true
                    }
                }
            }
            if (!ignoreBuildings && isBuilding && way.isClosed()) {
                buildings.add(new Building(way, height))
                nb_buildings++
            }
            if (!ignoreRoads && isRoad) {
                if (removeTunnels && isTunnel) {
                    return
                }
                roads.add(new Road(way))
                nb_roads++
            }
            if (!ignoreGround && !isBuilding && !isRoad && way.isClosed()) {
                grounds.add(new Ground(way))
                nb_grounds++
            }
        } else if (entityContainer instanceof RelationContainer) {
            nb_relations++
            Relation rel = ((RelationContainer) entityContainer).getEntity()
            relations.put(rel.getId(), rel)
        } else {
            System.out.println("Unknown Entity!")
        }
    }

    @Override
    void complete() {
        for (Building building : buildings) {
            building.setGeom(calculateBuildingGeometry(building.way))
        }
        for (Road road : roads) {
            road.setGeom(calculateRoadGeometry(road.way))
        }
        GeometryFactory geomFactory = new GeometryFactory()
        for (Ground ground : grounds) {
            if (ground.priority == 0) {
                ground.setGeom(geomFactory.createPolygon())
                continue
            }
            Geometry geom = calculateGroundGeometry(ground.way)
            ground.setGeom(geom)
        }
        int doPrint = 2
        for (int j = 0; j < grounds.size(); j++) {
            if (j >= doPrint) {
                logger.info("Cleaning GROUND geom : " + j + "/" + grounds.size())
                doPrint *= 2
            }
            if (grounds[j].geom.isEmpty() || !grounds[j].geom.isValid()) {
                continue
            }
            if (!["Polygon", "MultiPolygon"].contains(grounds[j].geom.geometryType)) {
                continue
            }
            for (int k = 0; k < grounds.size(); k++) {
                if (j == k) {
                    continue
                }
                if (grounds[k].geom.isEmpty() || !grounds[k].geom.isValid()) {
                    continue
                }
                if (!["Polygon", "MultiPolygon"].contains(grounds[k].geom.geometryType)) {
                    continue
                }
                if (!grounds[j].geom.intersects(grounds[k].geom)) {
                    continue
                }
                if (grounds[j].priority >= grounds[k].priority) {
                    grounds[k].geom = grounds[k].geom.difference(grounds[j].geom)
                }
                if (grounds[j].priority < grounds[k].priority) {
                    grounds[j].geom = grounds[j].geom.difference(grounds[k].geom)
                }
            }
        }
    }

    @Override
    void close() {}

    Geometry calculateBuildingGeometry(Way way) {
        GeometryFactory geomFactory = new GeometryFactory()
        if (way == null) {
            return geomFactory.createPolygon()
        }
        List<WayNode> wayNodes = way.getWayNodes()
        if (wayNodes.size() < 4) {
            return geomFactory.createPolygon()
        }
        Coordinate[] shell = new Coordinate[wayNodes.size()]
        for (int i = 0; i < wayNodes.size(); i++) {
            Node node = nodes.get(wayNodes.get(i).getNodeId())
            double x = node.getLongitude()
            double y = node.getLatitude()
            shell[i] = new Coordinate(x, y, 0.0)
        }
        return geomFactory.createPolygon(shell)
    }

    Geometry calculateRoadGeometry(Way way) {
        GeometryFactory geomFactory = new GeometryFactory()
        if (way == null) {
            return geomFactory.createLineString()
        }
        List<WayNode> wayNodes = way.getWayNodes()
        if (wayNodes.size() < 2) {
            return geomFactory.createLineString()
        }
        Coordinate[] coordinates = new Coordinate[wayNodes.size()]
        for (int i = 0; i < wayNodes.size(); i++) {
            Node node = nodes.get(wayNodes.get(i).getNodeId())
            double x = node.getLongitude()
            double y = node.getLatitude()
            coordinates[i] = new Coordinate(x, y, 0.0)
        }
        return geomFactory.createLineString(coordinates)
    }

    Geometry calculateGroundGeometry(Way way) {
        GeometryFactory geomFactory = new GeometryFactory()
        if (way == null) {
            return geomFactory.createPolygon()
        }
        List<WayNode> wayNodes = way.getWayNodes()
        if (wayNodes.size() < 4) {
            return geomFactory.createPolygon()
        }
        Coordinate[] shell = new Coordinate[wayNodes.size()]
        for (int i = 0; i < wayNodes.size(); i++) {
            Node node = nodes.get(wayNodes.get(i).getNodeId())
            double x = node.getLongitude()
            double y = node.getLatitude()
            shell[i] = new Coordinate(x, y, 0.0)
        }
        return geomFactory.createPolygon(shell)
    }
}


class Building {

    long id
    Way way
    Geometry geom
    double height = 0.0

    Building(Way way) {
        this.way = way
        this.id = way.getId()
        double h = 4.0 + rand.nextDouble() * 2.1
        boolean trueHeightFound = false
        for (Tag tag : way.getTags()) {
            if (!trueHeightFound && "building:levels".equalsIgnoreCase(tag.getKey())) {
                h = h - 4 + Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", "")) * 3.0
            }
            if ("height".equalsIgnoreCase(tag.getKey())) {
                h = Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", ""))
                trueHeightFound = true
            }
        }
        this.height = h
    }

    Building(Way way, double height) {
        this.way = way
        this.id = way.getId()
        this.height = height
    }

    void setGeom(Geometry geom) {
        this.geom = geom
    }

    void setHeight(double height) {
        this.height = height
    }
}

class Road {

    def static aadf_d = [26103, 17936, 7124, 1400, 700, 350, 175]
    def static aadf_e = [7458, 3826, 1069, 400, 200, 100, 50]
    def static aadf_n = [3729, 2152, 712, 200, 100, 50, 25]
    def static hv_d = [0.25, 0.2, 0.2, 0.15, 0.10, 0.05, 0.02]
    def static hv_e = [0.35, 0.2, 0.15, 0.10, 0.06, 0.02, 0.01]
    def static hv_n = [0.45, 0.2, 0.1, 0.05, 0.03, 0.01, 0.0]
    def static speed = [130, 110, 80, 80, 50, 30, 30]

    def static hours_in_d = 12
    def static hours_in_e = 4
    def static hours_in_n = 8

    long id
    Way way
    Geometry geom
    double maxspeed = 0.0
    boolean oneway = false
    String type = null
    int category = 5

    Road(Way way) {
        this.way = way
        this.id = way.getId()
        for (Tag tag : way.getTags()) {
            if ("maxspeed".equalsIgnoreCase(tag.getKey())) {
                try {
                    this.maxspeed = Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", ""))
                } catch (NumberFormatException e) {
                    // in case maxspeed does not contain a numerical value
                }
                if (tag.getValue().contains("mph")) {
                    maxspeed = maxspeed * 1.60934
                }
            }
            if ("highway".equalsIgnoreCase(tag.getKey())) {
                this.type = tag.getValue()
            }
            if ("highway".equalsIgnoreCase(tag.getKey()) && "yes".equalsIgnoreCase(tag.getValue())) {
                oneway = true
            }
        }
        updateCategory()
    }

    double getNbLV(String period) {
        double lv
        if (period == "d") {
            lv = (1 - hv_d[category]) * aadf_d[category] / hours_in_d
        } else if (period == "e") {
            lv = (1 - hv_e[category]) * aadf_e[category] / hours_in_e
        } else { // n
            lv = (1 - hv_n[category]) * aadf_n[category] / hours_in_n
        }
        if (oneway) {
            lv /= 2
        }
        return lv
    }

    double getNbHV(String period) {
        double hv
        if (period == "d") {
            hv = hv_d[category] * aadf_d[category] / hours_in_d
        } else if (period == "e") {
            hv = hv_e[category] * aadf_e[category] / hours_in_e
        } else { // n
            hv = hv_n[category] * aadf_n[category] / hours_in_n
        }
        if (oneway) {
            hv /= 2
        }
        return hv
    }

    void updateCategory() {
        if (["motorway", "motorway_link"].contains(type)) {
            category = 0
        }
        if (["trunk", "trunk_link"].contains(type)) {
            category = 1
        }
        if (["primary", "primary_link"].contains(type)) {
            category = 2
        }
        if (["secondary", "secondary_link"].contains(type)) {
            category = 3
        }
        if (["tertiary", "tertiary_link", "unclassified"].contains(type)) {
            category = 4
        }
        if (["residential"].contains(type)) {
            category = 5
        }
        if (["service", "living_street"].contains(type)) {
            category = 6
        }
    }

    void setGeom(Geometry geom) {
        this.geom = geom
    }

    void setHeight(double height) {
        this.height = height
    }
}

class Ground {

    long id
    Way way
    Geometry geom

    int priority = 0
    float coeff_G = 0.0

    Ground(Way way) {
        this.way = way
        this.id = way.getId()

        String primaryTagKey = ""
        String primaryTagValue = ""
        String secondaryTagKey = ""
        String secondaryTagValue = ""

        for (Tag tag : way.getTags()) {
            String key = tag.getKey()
            String value = tag.getValue()
            if (["aeroway", "amenity", "landcover", "landuse", "leisure", "natural", "water", "waterway"].contains(key)) {
                primaryTagKey = key
                primaryTagValue = value
            }
            if (["parking", "covered", "surface", "wetland"].contains(key)) {
                secondaryTagKey = key
                secondaryTagValue = value
            }
        }
        if (primaryTagKey == "aeroway" && ["taxiway", "runway", "aerodrome", "helipad", "apron", "taxilane"].contains(primaryTagValue)) {
            priority = 29
            coeff_G = 0.1
        }
        if (primaryTagKey == "amenity") {
            if (primaryTagValue == "taxi") {
                priority = 22
                coeff_G = 0.1
            }
            if (primaryTagValue == "parking" && secondaryTagKey == "parking" && !secondaryTagValue.contains("underground")) {
                priority = 22
                coeff_G = 0.1
            }
        }
        if (primaryTagKey == "landcover") {
            if (primaryTagValue == "water") {
                priority = 7
                coeff_G = 0.3
            }
            if (["bedrock", "bare_ground", "concrete", "asphalt"].contains(primaryTagValue)) {
                priority = 8
                coeff_G = 0.1
            }
            if (primaryTagValue == "sand") {
                priority = 9
                coeff_G = 0.2
            }
            if (["scrub", "gravel"].contains(primaryTagValue)) {
                priority = 10
                coeff_G = 0.7
            }
            if (["bushes", "vegetation"].contains(primaryTagValue)) {
                priority = 11
                coeff_G = 0.8
            }
            if (["flowerbed", "trees, grass", "trees", "grass", "tree", "grassland", "wood"].contains(primaryTagValue)) {
                priority = 12
                coeff_G = 1.0
            }
        }
        if (primaryTagKey == "landuse") {
            if (primaryTagValue == "reservoir" && secondaryTagKey == "covered" && secondaryTagValue == "no") {
                priority = 7
                coeff_G = 0.3
            }
            if (["residential", "industrial", "retail", "harbour", "quarry", "landfill",
                 "construction", "commercial", "garages", "railway", "basin", "farmyard"].contains(primaryTagValue)) {
                priority = 23
                coeff_G = 0.1
            }
            if (primaryTagValue == "brownfield") {
                priority = 24
                coeff_G = 0.3
            }
            if (primaryTagValue == "salt_pond") {
                priority = 25
                coeff_G = 0.5
            }
            if (["farmland", "allotements", "logging", "plant_nursery", "farm"].contains(primaryTagValue)) {
                priority = 26
                coeff_G = 0.7
            }
            if (["vineyard", "orchard", "greenfield", "village_green"].contains(primaryTagValue)) {
                priority = 27
                coeff_G = 0.8
            }
            if (["meadow", "forest", "grass"].contains(primaryTagValue)) {
                priority = 28
                coeff_G = 1.0
            }
        }
        if (primaryTagKey == "leisure") {
            if (primaryTagValue == "pitch" && secondaryTagKey == "surface") {
                if (["asphalt", "concrete", "concrete:plate"].contains(secondaryTagValue)) {
                    priority = 1
                    coeff_G = 0.1
                }
                if (["dirt", "compacted", "sand", "wood", "clay"].contains(secondaryTagValue)) {
                    priority = 2
                    coeff_G = 0.2
                }
                if (["ground", "fine_gravel", "earth", "mud"].contains(secondaryTagValue)) {
                    priority = 4
                    coeff_G = 0.5
                }
                if (["gravel"].contains(secondaryTagValue)) {
                    priority = 5
                    coeff_G = 0.7
                }
                if (["grass"].contains(secondaryTagValue)) {
                    priority = 6
                    coeff_G = 1.0
                }
            }
            if (primaryTagValue == "marina") {
                priority = 30
                coeff_G = 0.2
            }
            if (primaryTagValue == "park") {
                priority = 31
                coeff_G = 0.7
            }
            if (["garden", "nature_reserve", "golf_course"].contains(primaryTagValue)) {
                priority = 32
                coeff_G = 1.0
            }
        }
        if (primaryTagKey == "natural") {
            if (primaryTagValue == "beach" && secondaryTagKey == "surface") {
                if (secondaryTagValue == "sand") {
                    priority = 2
                    coeff_G = 0.2
                }
                if (secondaryTagValue == "shingle") {
                    priority = 3
                    coeff_G = 0.3
                }
                if (secondaryTagValue == "gravel" || secondaryTagValue == "pebbles") {
                    priority = 5
                    coeff_G = 0.7
                }
            }
            if (primaryTagValue == "wetland" && secondaryTagKey == "wetland") {
                if (secondaryTagValue == "tidalflat") {
                    priority = 14
                    coeff_G = 0.2
                }
                if (secondaryTagValue == "saltern") {
                    priority = 15
                    coeff_G = 0.3
                }
                if (secondaryTagValue == "marsh") {
                    priority = 16
                    coeff_G = 0.4
                }
                if (secondaryTagValue == "reebed") {
                    priority = 18
                    coeff_G = 0.6
                }
                if (secondaryTagValue == "bog") {
                    priority = 19
                    coeff_G = 0.7
                }
                if (secondaryTagValue == "mangrove") {
                    priority = 21
                    coeff_G = 1.0
                }
                if (["swamp", "saltmarsh", "wet_meadow"].contains(secondaryTagValue)) {
                    priority = 20
                    coeff_G = 0.9
                }
            }
            if (primaryTagValue == "bare_rock") {
                priority = 13
                coeff_G = 0.1
            }
            if (primaryTagValue == "bay") {
                priority = 7
                coeff_G = 0.3
            }
            if (primaryTagValue == "glacier") {
                priority = 13
                coeff_G = 0.1
            }
            if (primaryTagValue == "heath" || primaryTagValue == "grassland") {
                priority = 21
                coeff_G = 1.0
            }
            if (primaryTagValue == "rock") {
                priority = 13
                coeff_G = 0.1
            }
            if (primaryTagValue == "sand") {
                priority = 14
                coeff_G = 0.2
            }
            if (primaryTagValue == "scree") {
                priority = 17
                coeff_G = 0.5
            }
            if (primaryTagValue == "scrub") {
                priority = 19
                coeff_G = 0.7
            }
            if (primaryTagValue == "shingle") {
                priority = 15
                coeff_G = 0.3
            }
            if (primaryTagValue == "water") {
                priority = 7
                coeff_G = 0.3
            }
            if (primaryTagValue == "wood") {
                priority = 21
                coeff_G = 1.0
            }
        }
        if (primaryTagKey == "water") {
            if (["pond", "lake", "reservoir", "river", "wastewater", "canal", "oxbow",
                 "salt", "lagoon", "yes", "ditch", "salt_pool", "tidal", "stream",
                 "fishpond", "riverbank", "pool", "lock", "natural", "shallow",
                 "salt_pond", "lake;pond", "marsh", "well", "reflecting_pool",
                 "fountain", "stream;river", "not_deep"].contains(primaryTagValue)) {
                priority = 7
                coeff_G = 0.3
            }
        }
        if (primaryTagKey == "waterway") {
            if (["stream", "riverbank", "canal", "artificial"].contains(primaryTagValue)) {
                priority = 7
                coeff_G = 0.3
            }
        }
    }

    void setGeom(Geometry geom) {
        this.geom = geom
    }
}

