package com.acclima.backend2

import cats.effect.{IO, IOApp}

object Main extends IOApp.Simple:
  val run = Backend2Server.run[IO]
