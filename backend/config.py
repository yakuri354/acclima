from os import environ as e

DB_HOST = e.get("DB_HOST", "localhost:25432")
DB_NAME = e.get("DB_NAME", "acclima")
DB_USER = e.get("DB_USER", "acclima")
DB_PASS = e.get("DB_PASS", "acclimapgpass")

WAQI_TOKEN = e.get("WAQI_TOKEN", "")
OWM_TOKEN = e.get("OWM_TOKEN", "")