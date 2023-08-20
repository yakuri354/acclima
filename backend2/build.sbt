val Http4sVersion = "1.0.0-M40"
val MunitVersion = "1.0.0-M8"
val LogbackVersion = "1.3.8"
val circeVersion = "0.14.0"
val MunitCatsEffectVersion = "2.0.0-M3"
val osmosisVersion = "0.48.3"

lazy val root = (project in file("."))
  .settings(
    organization := "com.acclima",
    name := "backend2",
    version := "0.0.1-SNAPSHOT",
    scalaVersion := "3.3.0",

    resolvers ++= Seq(
      "osgeo" at "https://repo.osgeo.org/repository/release/",
      "osgeo-tools" at "https://download.osgeo.org/webdav/geotools/",
      "geo-solutions" at "https://maven.geo-solutions.it/",
      "sonatype-snapshots" at "https://oss.sonatype.org/content/repositories/snapshots/",
      "sonatype-releases" at "https://oss.sonatype.org/content/repositories/releases/",
      "matsim" at "https://oss.sonatype.org/content/repositories/snapshots/"
    ),

    libraryDependencies ++= Seq(
      "org.http4s" %% "http4s-ember-server",
      "org.http4s" %% "http4s-ember-client",
      "org.http4s" %% "http4s-circe",
      "org.http4s" %% "http4s-dsl",
    ).map(_ % Http4sVersion),

    libraryDependencies ++= Seq(
      "io.circe" %% "circe-core",
      "io.circe" %% "circe-generic",
      "io.circe" %% "circe-parser",
    ).map(_ % circeVersion),

    libraryDependencies ++= Seq(
      "org.openstreetmap.osmosis" % "osmosis-core",
      "org.openstreetmap.osmosis" % "osmosis-pbf",
      "org.openstreetmap.osmosis" % "osmosis-xml",
    ).map(_ % osmosisVersion),

    libraryDependencies ++= Seq(
      "org.scalameta" %% "munit" % MunitVersion % Test,
      "org.typelevel" %% "munit-cats-effect" % MunitCatsEffectVersion % Test,
      "com.acervera.osm4scala" % "osm4scala-core_2.13" % "1.0.11"
    ),

    testFrameworks += new TestFramework("munit.Framework")
  )
