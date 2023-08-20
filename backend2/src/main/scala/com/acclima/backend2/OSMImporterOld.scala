/** NoiseModelling is an open-source tool designed to produce environmental
  * noise maps on very large urban areas. It can be used as a Java library or be
  * controlled through a user friendly web interface.
  *
  * This version is developed by Université Gustave Eiffel and CNRS
  * <http://noise-planet.org/noisemodelling.html>
  *
  * NoiseModelling is distributed under GPL 3 license. You can read a copy of
  * this License in the file LICENCE provided with this software.
  *
  * Contact: contact@noise-planet.org
  */
/** @Author
  *   Valentin Le Bescond, Université Gustave Eiffel
  * @Author
  *   Nicolas Fortin, Université Gustave Eiffel
  * @Author
  *   Gwendall Petit, Cerema
  */

package com.acclima.backend2

import cats.effect.IO
import org.openstreetmap.osmosis.core.task.v0_6.RunnableSource

class OSMImporterOld:
  def loadOSMData(reader: RunnableSource, sql: Sql, tableName: String): IO[Unit] =
    val srid = 3857 // TODO

    logger.info("Start : Get Buildings from OSM")
    logger.info("inputs {}")
    val handler = new OsmHandler(logger, false, false, false, false)
    reader.setSink(handler)
    reader.run()
    logger.info("OSM Read done")
    sql.execute(
      "DROP TABLE IF EXISTS ?",
      new util.ArrayList[String](java.util.Arrays.asList(tableName))
    )
    sql.execute(
      "CREATE TABLE ? ( \n        ID_WAY integer PRIMARY KEY, \n        THE_GEOM geometry,\n        HEIGHT real\n    );",
      new util.ArrayList[String](java.util.Arrays.asList(tableName))
    )
    for (building <- handler.buildings) {
// sql.execute("INSERT INTO " + tableName + " VALUES (" + building.id + ", ST_MakeValid(ST_SIMPLIFYPRESERVETOPOLOGY(ST_Transform(ST_GeomFromText('" + building.geom + "', 4326), " + srid + "),0.1)), " + building.height + ")")
      sql.execute(
        "INSERT INTO ? VALUES (?, ST_MakeValid(ST_SIMPLIFYPRESERVETOPOLOGY(ST_Transform(ST_GeomFromText(?, 4326), ?),0.1)), ?)",
        new util.ArrayList[AnyRef](
          java.util.Arrays.asList(
            tableName,
            building.getId,
            building.getGeom,
            srid,
            building.getHeight
          )
        )
      )
    }
    sql.execute(
      "\n        CREATE SPATIAL INDEX IF NOT EXISTS BUILDINGS_INDEX ON ? (the_geom);\n        -- List buildings that intersects with other buildings that have a greater area\n        DROP TABLE IF EXISTS tmp_relation_buildings_buildings;\n        CREATE TABLE tmp_relation_buildings_buildings AS SELECT s1.ID_WAY as PK_BUILDING, S2.ID_WAY as PK2_BUILDING FROM MAP_BUILDINGS_GEOM S1, MAP_BUILDINGS_GEOM S2 WHERE ST_AREA(S1.THE_GEOM) < ST_AREA(S2.THE_GEOM) AND S1.THE_GEOM && S2.THE_GEOM AND ST_DISTANCE(S1.THE_GEOM, S2.THE_GEOM) <= 0.1;\n        \n        -- Alter that small area buildings by removing shared area\n        DROP TABLE IF EXISTS tmp_buildings_truncated;\n        CREATE TABLE tmp_buildings_truncated AS SELECT PK_BUILDING, ST_DIFFERENCE(s1.the_geom, ST_BUFFER(ST_Collect(s2.the_geom), 0.1, 'join=mitre')) the_geom, s1.HEIGHT HEIGHT from tmp_relation_buildings_buildings r, MAP_BUILDINGS_GEOM s1, MAP_BUILDINGS_GEOM s2 WHERE PK_BUILDING = S1.ID_WAY AND PK2_BUILDING = S2.ID_WAY  GROUP BY PK_BUILDING;\n        \n        -- Merge original buildings with altered buildings \n        DROP TABLE IF EXISTS BUILDINGS;\n        CREATE TABLE BUILDINGS(PK INTEGER PRIMARY KEY, THE_GEOM GEOMETRY, HEIGHT real);\n        SELECT s.id_way, ST_SETSRID(s.the_geom, ''' + srid + '''), s.HEIGHT into BUILDINGS from MAP_BUILDINGS_GEOM s where id_way not in (select PK_BUILDING from tmp_buildings_truncated) UNION ALL select PK_BUILDING, ST_SETSRID(the_geom, ''' + srid + '''), HEIGHT from tmp_buildings_truncated WHERE NOT st_isempty(the_geom);\n\n        DROP TABLE IF EXISTS tmp_buildings_truncated;\n        DROP TABLE IF EXISTS tmp_relation_buildings_buildings;\n        DROP TABLE IF EXISTS MAP_BUILDINGS_GEOM;\n    ",
      new util.ArrayList[String](java.util.Arrays.asList(tableName))
    )
    sql.execute(
      "CREATE SPATIAL INDEX IF NOT EXISTS BUILDING_GEOM_INDEX ON BUILDINGS(THE_GEOM)"
    )
    sql.execute("DROP TABLE IF EXISTS ROADS")
    sql.execute(
      "CREATE TABLE ROADS (PK serial PRIMARY KEY, ID_WAY integer, THE_GEOM geometry, TYPE varchar, LV_D integer, LV_E integer,LV_N integer,HV_D integer,HV_E integer,HV_N integer,LV_SPD_D integer,LV_SPD_E integer,LV_SPD_N integer,HV_SPD_D integer, HV_SPD_E integer,HV_SPD_N integer, PVMT varchar(10));"
    )
    import scala.collection.JavaConversions.*
    for (road <- handler.roads) {
      if (road.getGeom.invokeMethod("isEmpty", new Array[AnyRef](0)).asBoolean)
        continue // todo: continue is not supported
      val query =
        "INSERT INTO ROADS(ID_WAY, THE_GEOM, TYPE, LV_D, LV_E, LV_N, HV_D, HV_E, HV_N, LV_SPD_D, LV_SPD_E, LV_SPD_N, HV_SPD_D, HV_SPD_E, HV_SPD_N, PVMT) VALUES (?, st_setsrid(st_updatez(ST_precisionreducer(ST_SIMPLIFYPRESERVETOPOLOGY(ST_TRANSFORM(ST_GeomFromText(?, 4326), ?),0.1),1), 0.05), ?),?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
      sql.execute(
        query,
        new util.ArrayList[AnyRef](
          java.util.Arrays.asList(
            road.getId,
            road.getGeom,
            srid,
            srid,
            road.getType,
            road.getNbLV("d"),
            road.getNbLV("e"),
            road.getNbLV("n"),
            road.getNbHV("d"),
            road.getNbHV("e"),
            road.getNbHV("n"),
            com.acclima.backend2.Road.getSpeed.get(road.getCategory),
            com.acclima.backend2.Road.getSpeed.get(road.getCategory),
            com.acclima.backend2.Road.getSpeed.get(road.getCategory),
            java.lang.Math.min(
              90,
              com.acclima.backend2.Road.getSpeed.get(road.getCategory)
            ),
            java.lang.Math.min(
              90,
              com.acclima.backend2.Road.getSpeed.get(road.getCategory)
            ),
            java.lang.Math.min(
              90,
              com.acclima.backend2.Road.getSpeed.get(road.getCategory)
            ),
            "NL08"
          )
        )
      )
    }
    sql.execute(
      "CREATE SPATIAL INDEX IF NOT EXISTS ROADS_GEOM_INDEX ON " + "ROADS" + "(THE_GEOM)"
    )
    sql.execute("DROP TABLE IF EXISTS GROUND")
    sql.execute(
      "CREATE TABLE GROUND (PK serial PRIMARY KEY, ID_WAY int, THE_GEOM geometry, PRIORITY int, G double);"
    )
    import scala.collection.JavaConversions.*
    for (ground <- handler.grounds) {
      if (ground.getPriority == 0) continue // todo: continue is not supported
      if (
        ground.getGeom.invokeMethod("isEmpty", new Array[AnyRef](0)).asBoolean
      ) continue // todo: continue is not supported
// sql.execute("INSERT INTO GROUND (ID_WAY, THE_GEOM, PRIORITY, G) VALUES (" + ground.id + ", ST_Transform(ST_GeomFromText('" + ground.geom + "', 4326), " + srid + "), " + ground.priority + ", " + ground.coeff_G + ")")
      sql.execute(
        "INSERT INTO GROUND (ID_WAY, THE_GEOM, PRIORITY, G) VALUES (?, ST_Transform(ST_GeomFromText(?, 4326), ?), ?, ?)",
        new util.ArrayList[AnyRef](
          java.util.Arrays.asList(
            ground.getId,
            ground.getGeom,
            srid,
            ground.getPriority,
            ground.getCoeff_G
          )
        )
      )
    }
    sql.execute(
      "CREATE SPATIAL INDEX IF NOT EXISTS GROUND_GEOM_INDEX ON GROUND(THE_GEOM)"
    )

    logger.info("SQL INSERT done")

    logger.info("Result : " + this.getBinding.getProperty("resultString"))

