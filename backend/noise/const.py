MAX_BUILDING_SEARCH_DIST = 1000  # m

# TODO fix
AREA_RADIUS = 500  # m

RECEIVER_BUFFER_SIZE = 3.0  # m

# FIXME ground
# OVERPASS_TAGS = ["building", "highway", "aeroway", "amenity", "landcover", "landuse", "leisure", "natural", "water", "waterway"]
OVERPASS_TAGS = ["building", "highway"]

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

# hardcoded in noisemodelling
BUILDINGS_TABLE = "BUILDINGS"
ROADS_TABLE = "ROADS"
GROUND_TABLE = "GROUND"
LW_ROADS_TABLE = "LW_ROADS"
RECEIVERS_TABLE = "RECEIVERS"

LDEN_GEOM_TABLE = "LDEN_GEOM"
LDAY_GEOM_TABLE = "LDAY_GEOM"
LEVENING_GEOM_TABLE = "LEVENING_GEOM"
LNIGHT_GEOM_TABLE = "LNIGHT_GEOM"


SRID_ANGLE = 4326  # OSM
SRID_FLAT = 3857

OSM_SRID = SRID_ANGLE

SRID_H2DB = SRID_FLAT


CACHE_DIST_TRESHOLD = 10  # m
