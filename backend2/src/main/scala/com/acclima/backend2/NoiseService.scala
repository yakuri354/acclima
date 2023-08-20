package com.acclima.backend2
import cats.effect.IO
import org.http4s.Request
import org.http4s.client.Client
import org.http4s.Uri

case class NoiseData(day: Double, evening: Double, night: Double, den: Double)


class NoiseService extends GeoService[NoiseData]:


  override def getData(pos: Coordinate)(client: Client[IO]): IO[Either[Throwable, NoiseData]] =
    IO.pure(Left(NotImplementedError("sorry")))