package com.acclima.backend2;

public class OsmHandler implements org.openstreetmap.osmosis.core.task.v0_6.Sink {
    public OsmHandler(org.slf4j.Logger logger, boolean ignoreBuildings, boolean ignoreRoads, boolean ignoreGround, boolean removeTunnels) {
        this.logger = logger;
        this.ignoreBuildings = ignoreBuildings;
        this.ignoreRoads = ignoreRoads;
        this.ignoreGround = ignoreGround;
        this.removeTunnels = removeTunnels;
    }

    @java.lang.Override
    public void initialize(java.util.Map<java.lang.String, java.lang.Object> arg0) {
    }

    @java.lang.Override
    public void process(org.openstreetmap.osmosis.core.container.v0_6.EntityContainer entityContainer) {
        if (entityContainer instanceof org.openstreetmap.osmosis.core.container.v0_6.NodeContainer) {
            nb_nodes++;
            org.openstreetmap.osmosis.core.domain.v0_6.Node node = ((org.openstreetmap.osmosis.core.container.v0_6.NodeContainer) entityContainer).getEntity();
            nodes.put(node.getId(), node);
        } else if (entityContainer instanceof org.openstreetmap.osmosis.core.container.v0_6.WayContainer) {
            nb_ways++;
            org.openstreetmap.osmosis.core.domain.v0_6.Way way = ((org.openstreetmap.osmosis.core.container.v0_6.WayContainer) entityContainer).getEntity();
            ways.put(way.getId(), way);
            boolean isBuilding = false;
            boolean isRoad = false;
            boolean isTunnel = false;
            double height = 4.0 + rand.nextDouble() * 2.1;
            boolean trueHeightFound = false;
            for (org.openstreetmap.osmosis.core.domain.v0_6.Tag tag : way.getTags()) {
                if ("building".equalsIgnoreCase(tag.getKey())) {
                    isBuilding = true;
                }

                if ("tunnel".equalsIgnoreCase(tag.getKey()) && "yes".equalsIgnoreCase(tag.getValue())) {
                    isTunnel = true;
                }

                if ("highway".equalsIgnoreCase((tag.getKey()))) {
                    isRoad = true;
                }

                if (isBuilding) {
                    if (!trueHeightFound && "building:levels".equalsIgnoreCase(tag.getKey())) {
                        height = height - 4 + java.lang.Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", "")) * 3.0;
                    }

                    if ("height".equalsIgnoreCase(tag.getKey())) {
                        height = java.lang.Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", ""));
                        trueHeightFound = true;
                    }

                }

            }

            if (!ignoreBuildings && isBuilding && way.isClosed()) {
                buildings.add(new com.acclima.backend2.Building(way, height));
                nb_buildings++;
            }

            if (!ignoreRoads && isRoad) {
                if (removeTunnels && isTunnel) {
                    return;

                }

                roads.add(new com.acclima.backend2.Road(way));
                nb_roads++;
            }

            if (!ignoreGround && !isBuilding && !isRoad && way.isClosed()) {
                grounds.add(new com.acclima.backend2.Ground(way));
                nb_grounds++;
            }

        } else if (entityContainer instanceof org.openstreetmap.osmosis.core.container.v0_6.RelationContainer) {
            nb_relations++;
            org.openstreetmap.osmosis.core.domain.v0_6.Relation rel = ((org.openstreetmap.osmosis.core.container.v0_6.RelationContainer) entityContainer).getEntity();
            relations.put(rel.getId(), rel);
        } else {
            java.lang.System.out.println("Unknown Entity!");
        }

    }

    @java.lang.Override
    public void complete() {
        for (com.acclima.backend2.Building building : buildings) {
            building.setGeom(calculateBuildingGeometry(building.getWay()));
        }

        for (com.acclima.backend2.Road road : roads) {
            road.setGeom(calculateRoadGeometry(road.getWay()));
        }

        GeometryFactory geomFactory = new GeometryFactory();
        for (com.acclima.backend2.Ground ground : grounds) {
            if (ground.getPriority() == 0) {
                ground.setGeom(geomFactory.invokeMethod("createPolygon", new java.lang.Object[0]));
                continue;
            }

            Geometry geom = calculateGroundGeometry(ground.getWay());
            ground.setGeom(geom);
        }

        int doPrint = 2;
        for (int j = 0; j < grounds.size(); j++) {
            if (j >= doPrint) {
                logger.info("Cleaning GROUND geom : " + j + "/" + grounds.size());
                doPrint *= 2;
            }

            if (grounds.get(j).getGeom().invokeMethod("isEmpty", new java.lang.Object[0]) || !org.codehaus.groovy.runtime.DefaultGroovyMethods.asBoolean(grounds.get(j).getGeom().invokeMethod("isValid", new java.lang.Object[0]))) {
                continue;
            }

            if (!new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("Polygon", "MultiPolygon")).contains(grounds.get(j).getGeom().geometryType)) {
                continue;
            }

            for (int k = 0; k < grounds.size(); k++) {
                if (j == k) {
                    continue;
                }

                if (grounds.get(k).getGeom().invokeMethod("isEmpty", new java.lang.Object[0]) || !org.codehaus.groovy.runtime.DefaultGroovyMethods.asBoolean(grounds.get(k).getGeom().invokeMethod("isValid", new java.lang.Object[0]))) {
                    continue;
                }

                if (!new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("Polygon", "MultiPolygon")).contains(grounds.get(k).getGeom().geometryType)) {
                    continue;
                }

                if (!org.codehaus.groovy.runtime.DefaultGroovyMethods.asBoolean(grounds.get(j).getGeom().invokeMethod("intersects", new java.lang.Object[]{grounds.get(k).getGeom()}))) {
                    continue;
                }

                if (grounds.get(j).getPriority() >= grounds.get(k).getPriority()) {
                    grounds.get(k).setGeom(grounds.get(k).getGeom().invokeMethod("difference", new java.lang.Object[]{grounds.get(j).getGeom()}));
                }

                if (grounds.get(j).getPriority() < grounds.get(k).getPriority()) {
                    grounds.get(j).setGeom(grounds.get(j).getGeom().invokeMethod("difference", new java.lang.Object[]{grounds.get(k).getGeom()}));
                }

            }

        }

    }

    @java.lang.Override
    public void close() {
    }

    public Geometry calculateBuildingGeometry(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        GeometryFactory geomFactory = new GeometryFactory();
        if (way == null) {
            return ((Geometry) (geomFactory.invokeMethod("createPolygon", new java.lang.Object[0])));
        }

        java.util.List<org.openstreetmap.osmosis.core.domain.v0_6.WayNode> wayNodes = way.getWayNodes();
        if (wayNodes.size() < 4) {
            return ((Geometry) (geomFactory.invokeMethod("createPolygon", new java.lang.Object[0])));
        }

        com.acclima.backend2.Coordinate[] shell = new com.acclima.backend2.Coordinate[wayNodes.size()];
        for (int i = 0; i < wayNodes.size(); i++) {
            org.openstreetmap.osmosis.core.domain.v0_6.Node node = nodes.get(wayNodes.get(i).getNodeId());
            double x = node.getLongitude();
            double y = node.getLatitude();
            shell[i] = new com.acclima.backend2.Coordinate(x, y);
        }

        return ((Geometry) (geomFactory.invokeMethod("createPolygon", new java.lang.Object[]{shell})));
    }

    public Geometry calculateRoadGeometry(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        GeometryFactory geomFactory = new GeometryFactory();
        if (way == null) {
            return ((Geometry) (geomFactory.invokeMethod("createLineString", new java.lang.Object[0])));
        }

        java.util.List<org.openstreetmap.osmosis.core.domain.v0_6.WayNode> wayNodes = way.getWayNodes();
        if (wayNodes.size() < 2) {
            return ((Geometry) (geomFactory.invokeMethod("createLineString", new java.lang.Object[0])));
        }

        com.acclima.backend2.Coordinate[] coordinates = new com.acclima.backend2.Coordinate[wayNodes.size()];
        for (int i = 0; i < wayNodes.size(); i++) {
            org.openstreetmap.osmosis.core.domain.v0_6.Node node = nodes.get(wayNodes.get(i).getNodeId());
            double x = node.getLongitude();
            double y = node.getLatitude();
            coordinates[i] = new com.acclima.backend2.Coordinate(x, y);
        }

        return ((Geometry) (geomFactory.invokeMethod("createLineString", new java.lang.Object[]{coordinates})));
    }

    public Geometry calculateGroundGeometry(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        GeometryFactory geomFactory = new GeometryFactory();
        if (way == null) {
            return ((Geometry) (geomFactory.invokeMethod("createPolygon", new java.lang.Object[0])));
        }

        java.util.List<org.openstreetmap.osmosis.core.domain.v0_6.WayNode> wayNodes = way.getWayNodes();
        if (wayNodes.size() < 4) {
            return ((Geometry) (geomFactory.invokeMethod("createPolygon", new java.lang.Object[0])));
        }

        com.acclima.backend2.Coordinate[] shell = new com.acclima.backend2.Coordinate[wayNodes.size()];
        for (int i = 0; i < wayNodes.size(); i++) {
            org.openstreetmap.osmosis.core.domain.v0_6.Node node = nodes.get(wayNodes.get(i).getNodeId());
            double x = node.getLongitude();
            double y = node.getLatitude();
            shell[i] = new com.acclima.backend2.Coordinate(x, y);
        }

        return ((Geometry) (geomFactory.invokeMethod("createPolygon", new java.lang.Object[]{shell})));
    }

    public java.util.Random getRand() {
        return rand;
    }

    public void setRand(java.util.Random rand) {
        this.rand = rand;
    }

    public org.slf4j.Logger getLogger() {
        return logger;
    }

    public void setLogger(org.slf4j.Logger logger) {
        this.logger = logger;
    }

    public boolean getIgnoreBuildings() {
        return ignoreBuildings;
    }

    public boolean isIgnoreBuildings() {
        return ignoreBuildings;
    }

    public void setIgnoreBuildings(boolean ignoreBuildings) {
        this.ignoreBuildings = ignoreBuildings;
    }

    public boolean getIgnoreRoads() {
        return ignoreRoads;
    }

    public boolean isIgnoreRoads() {
        return ignoreRoads;
    }

    public void setIgnoreRoads(boolean ignoreRoads) {
        this.ignoreRoads = ignoreRoads;
    }

    public boolean getIgnoreGround() {
        return ignoreGround;
    }

    public boolean isIgnoreGround() {
        return ignoreGround;
    }

    public void setIgnoreGround(boolean ignoreGround) {
        this.ignoreGround = ignoreGround;
    }

    public boolean getRemoveTunnels() {
        return removeTunnels;
    }

    public boolean isRemoveTunnels() {
        return removeTunnels;
    }

    public void setRemoveTunnels(boolean removeTunnels) {
        this.removeTunnels = removeTunnels;
    }

    public int nb_ways = 0;
    public int nb_nodes = 0;
    public int nb_relations = 0;
    public int nb_buildings = 0;
    public int nb_roads = 0;
    public int nb_grounds = 0;
    private java.util.Random rand = new java.util.Random();
    public java.util.Map<java.lang.Long, org.openstreetmap.osmosis.core.domain.v0_6.Node> nodes = new java.util.HashMap<java.lang.Long, org.openstreetmap.osmosis.core.domain.v0_6.Node>();
    public java.util.Map<java.lang.Long, org.openstreetmap.osmosis.core.domain.v0_6.Way> ways = new java.util.HashMap<java.lang.Long, org.openstreetmap.osmosis.core.domain.v0_6.Way>();
    public java.util.Map<java.lang.Long, org.openstreetmap.osmosis.core.domain.v0_6.Relation> relations = new java.util.HashMap<java.lang.Long, org.openstreetmap.osmosis.core.domain.v0_6.Relation>();
    public java.util.List<com.acclima.backend2.Building> buildings = new java.util.ArrayList<com.acclima.backend2.Building>();
    public java.util.List<com.acclima.backend2.Road> roads = new java.util.ArrayList<com.acclima.backend2.Road>();
    public java.util.List<com.acclima.backend2.Ground> grounds = new java.util.ArrayList<com.acclima.backend2.Ground>();
    private org.slf4j.Logger logger;
    private boolean ignoreBuildings;
    private boolean ignoreRoads;
    private boolean ignoreGround;
    private boolean removeTunnels;
}
