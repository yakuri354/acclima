package com.acclima.backend2

import java.time.Instant
import org.http4s.client.Client
import cats.effect.IO
import org.http4s.EntityDecoder
import org.http4s.EntityEncoder
import org.http4s.circe._
import io.circe.Json
import io.circe.Decoder
import cats.effect.Concurrent

case class AirData(dt: Instant, aqi: Double, components: Map[String, Double])

object AirData:
  given Decoder[AirData] = Decoder.instance(hc => {
    val data = hc.downField("list").downN(0)
    for {
      dt <- data.downField("dt").as[Long]
      aqi <- data.downField("main").downField("aqi").as[Double]
      comps <- data.downField("components").as[Map[String, Double]]
    } yield AirData(Instant.ofEpochSecond(dt), aqi, comps)
  })
  given [F[_]: Concurrent]: EntityDecoder[F, AirData] = jsonOf


val OWM_TOKEN = ""

class OSMAirService extends GeoService[AirData]:
  def getData(
      pos: Coordinate
  )(client: Client[cats.effect.IO]): IO[Either[Throwable, AirData]] =
    client.expect[AirData](
      s"https://api.openweathermap.org/data/2.5/air_pollution?lat=${pos.lat}&lon=${pos.lng}&appid=${OWM_TOKEN}"
    ).map(Right(_))
