package com.acclima.backend2

import cats.effect.IO

val overpassUrl = "https://overpass-api.de/api/interpreter"
val overpassQuery =
  """
    |(
    |  way[building]({{bbox}});
    |  way[highway]({{bbox}});
    |);
    |out meta;
    |>;
    |out meta qt;|
    |""".stripMargin

class OSMService {
  def downloadMap(poly: Seq[Coordinate]): IO[Either[Throwable, Unit]] =
    IO.pure(Right(()))

  def saveMap(): IO[Unit] =

}
