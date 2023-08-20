package com.acclima.backend2

import cats.effect.{Concurrent, IO}
import org.http4s.client.Client

import java.time.LocalDateTime
import java.util.Base64

case class LightApiError() extends RuntimeException
case class LightData(history: Seq[Double], elevation: Double)
object LightData:
  def fromApi(s: String): Either[Throwable, LightData] =
    s.split(',').toSeq match
      case data :: elev :: _ => Right(LightData(data.split(';').toSeq.map(_.toDouble), elev.toDouble))
      case _ => Left(LightApiError())

class LightPollutionMap extends GeoService[LightData]:
  override def getData(pos: Coordinate)(client: Client[IO]): IO[Either[Throwable, LightData]] =
    val key = Base64.getEncoder.encodeToString(
      (System.currentTimeMillis().toString + ";isuckdicks:)").getBytes
    )
    client.expect[String](
       s"https://www.lightpollutionmap.info/QueryRaster/?qk${key}&ql=viirs_2021&qt=point_t&qd=${pos.lng},${pos.lat}"
    ).map(s => LightData.fromApi(s))

