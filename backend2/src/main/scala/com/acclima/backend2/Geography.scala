package com.acclima.backend2

import cats.effect.IO
import org.http4s.{Request, Uri}
import org.http4s.client.Client

case class Coordinate(lat: Double, lng: Double)

trait GeoService[T]:
  def getData(pos: Coordinate)(client: Client[IO]): IO[Either[Throwable, T]]