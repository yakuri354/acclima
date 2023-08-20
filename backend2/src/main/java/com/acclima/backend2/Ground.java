public class Ground {
    public Ground(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        this.way = way;
        this.id = way.getId();

        java.lang.String primaryTagKey = "";
        java.lang.String primaryTagValue = "";
        java.lang.String secondaryTagKey = "";
        java.lang.String secondaryTagValue = "";

        for (org.openstreetmap.osmosis.core.domain.v0_6.Tag tag : way.getTags()) {
            java.lang.String key = tag.getKey();
            java.lang.String value = tag.getValue();
            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("aeroway", "amenity", "landcover", "landuse", "leisure", "natural", "water", "waterway")).contains(key)) {
                primaryTagKey = key;
                primaryTagValue = value;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("parking", "covered", "surface", "wetland")).contains(key)) {
                secondaryTagKey = key;
                secondaryTagValue = value;
            }

        }

        if (primaryTagKey.equals("aeroway") && new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("taxiway", "runway", "aerodrome", "helipad", "apron", "taxilane")).contains(primaryTagValue)) {
            priority = 29;
            coeff_G = 0.1;
        }

        if (primaryTagKey.equals("amenity")) {
            if (primaryTagValue.equals("taxi")) {
                priority = 22;
                coeff_G = 0.1;
            }

            if (primaryTagValue.equals("parking") && secondaryTagKey.equals("parking") && !secondaryTagValue.contains("underground")) {
                priority = 22;
                coeff_G = 0.1;
            }

        }

        if (primaryTagKey.equals("landcover")) {
            if (primaryTagValue.equals("water")) {
                priority = 7;
                coeff_G = 0.3;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("bedrock", "bare_ground", "concrete", "asphalt")).contains(primaryTagValue)) {
                priority = 8;
                coeff_G = 0.1;
            }

            if (primaryTagValue.equals("sand")) {
                priority = 9;
                coeff_G = 0.2;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("scrub", "gravel")).contains(primaryTagValue)) {
                priority = 10;
                coeff_G = 0.7;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("bushes", "vegetation")).contains(primaryTagValue)) {
                priority = 11;
                coeff_G = 0.8;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("flowerbed", "trees, grass", "trees", "grass", "tree", "grassland", "wood")).contains(primaryTagValue)) {
                priority = 12;
                coeff_G = 1.0;
            }

        }

        if (primaryTagKey.equals("landuse")) {
            if (primaryTagValue.equals("reservoir") && secondaryTagKey.equals("covered") && secondaryTagValue.equals("no")) {
                priority = 7;
                coeff_G = 0.3;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("residential", "industrial", "retail", "harbour", "quarry", "landfill", "construction", "commercial", "garages", "railway", "basin", "farmyard")).contains(primaryTagValue)) {
                priority = 23;
                coeff_G = 0.1;
            }

            if (primaryTagValue.equals("brownfield")) {
                priority = 24;
                coeff_G = 0.3;
            }

            if (primaryTagValue.equals("salt_pond")) {
                priority = 25;
                coeff_G = 0.5;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("farmland", "allotements", "logging", "plant_nursery", "farm")).contains(primaryTagValue)) {
                priority = 26;
                coeff_G = 0.7;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("vineyard", "orchard", "greenfield", "village_green")).contains(primaryTagValue)) {
                priority = 27;
                coeff_G = 0.8;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("meadow", "forest", "grass")).contains(primaryTagValue)) {
                priority = 28;
                coeff_G = 1.0;
            }

        }

        if (primaryTagKey.equals("leisure")) {
            if (primaryTagValue.equals("pitch") && secondaryTagKey.equals("surface")) {
                if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("asphalt", "concrete", "concrete:plate")).contains(secondaryTagValue)) {
                    priority = 1;
                    coeff_G = 0.1;
                }

                if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("dirt", "compacted", "sand", "wood", "clay")).contains(secondaryTagValue)) {
                    priority = 2;
                    coeff_G = 0.2;
                }

                if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("ground", "fine_gravel", "earth", "mud")).contains(secondaryTagValue)) {
                    priority = 4;
                    coeff_G = 0.5;
                }

                if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("gravel")).contains(secondaryTagValue)) {
                    priority = 5;
                    coeff_G = 0.7;
                }

                if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("grass")).contains(secondaryTagValue)) {
                    priority = 6;
                    coeff_G = 1.0;
                }

            }

            if (primaryTagValue.equals("marina")) {
                priority = 30;
                coeff_G = 0.2;
            }

            if (primaryTagValue.equals("park")) {
                priority = 31;
                coeff_G = 0.7;
            }

            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("garden", "nature_reserve", "golf_course")).contains(primaryTagValue)) {
                priority = 32;
                coeff_G = 1.0;
            }

        }

        if (primaryTagKey.equals("natural")) {
            if (primaryTagValue.equals("beach") && secondaryTagKey.equals("surface")) {
                if (secondaryTagValue.equals("sand")) {
                    priority = 2;
                    coeff_G = 0.2;
                }

                if (secondaryTagValue.equals("shingle")) {
                    priority = 3;
                    coeff_G = 0.3;
                }

                if (secondaryTagValue.equals("gravel") || secondaryTagValue.equals("pebbles")) {
                    priority = 5;
                    coeff_G = 0.7;
                }

            }

            if (primaryTagValue.equals("wetland") && secondaryTagKey.equals("wetland")) {
                if (secondaryTagValue.equals("tidalflat")) {
                    priority = 14;
                    coeff_G = 0.2;
                }

                if (secondaryTagValue.equals("saltern")) {
                    priority = 15;
                    coeff_G = 0.3;
                }

                if (secondaryTagValue.equals("marsh")) {
                    priority = 16;
                    coeff_G = 0.4;
                }

                if (secondaryTagValue.equals("reebed")) {
                    priority = 18;
                    coeff_G = 0.6;
                }

                if (secondaryTagValue.equals("bog")) {
                    priority = 19;
                    coeff_G = 0.7;
                }

                if (secondaryTagValue.equals("mangrove")) {
                    priority = 21;
                    coeff_G = 1.0;
                }

                if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("swamp", "saltmarsh", "wet_meadow")).contains(secondaryTagValue)) {
                    priority = 20;
                    coeff_G = 0.9;
                }

            }

            if (primaryTagValue.equals("bare_rock")) {
                priority = 13;
                coeff_G = 0.1;
            }

            if (primaryTagValue.equals("bay")) {
                priority = 7;
                coeff_G = 0.3;
            }

            if (primaryTagValue.equals("glacier")) {
                priority = 13;
                coeff_G = 0.1;
            }

            if (primaryTagValue.equals("heath") || primaryTagValue.equals("grassland")) {
                priority = 21;
                coeff_G = 1.0;
            }

            if (primaryTagValue.equals("rock")) {
                priority = 13;
                coeff_G = 0.1;
            }

            if (primaryTagValue.equals("sand")) {
                priority = 14;
                coeff_G = 0.2;
            }

            if (primaryTagValue.equals("scree")) {
                priority = 17;
                coeff_G = 0.5;
            }

            if (primaryTagValue.equals("scrub")) {
                priority = 19;
                coeff_G = 0.7;
            }

            if (primaryTagValue.equals("shingle")) {
                priority = 15;
                coeff_G = 0.3;
            }

            if (primaryTagValue.equals("water")) {
                priority = 7;
                coeff_G = 0.3;
            }

            if (primaryTagValue.equals("wood")) {
                priority = 21;
                coeff_G = 1.0;
            }

        }

        if (primaryTagKey.equals("water")) {
            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("pond", "lake", "reservoir", "river", "wastewater", "canal", "oxbow", "salt", "lagoon", "yes", "ditch", "salt_pool", "tidal", "stream", "fishpond", "riverbank", "pool", "lock", "natural", "shallow", "salt_pond", "lake;pond", "marsh", "well", "reflecting_pool", "fountain", "stream;river", "not_deep")).contains(primaryTagValue)) {
                priority = 7;
                coeff_G = 0.3;
            }

        }

        if (primaryTagKey.equals("waterway")) {
            if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("stream", "riverbank", "canal", "artificial")).contains(primaryTagValue)) {
                priority = 7;
                coeff_G = 0.3;
            }

        }

    }

    public void setGeom(Geometry geom) {
        this.geom = geom;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public org.openstreetmap.osmosis.core.domain.v0_6.Way getWay() {
        return way;
    }

    public void setWay(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        this.way = way;
    }

    public Geometry getGeom() {
        return geom;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public float getCoeff_G() {
        return coeff_G;
    }

    public void setCoeff_G(float coeff_G) {
        this.coeff_G = coeff_G;
    }

    private long id;
    private org.openstreetmap.osmosis.core.domain.v0_6.Way way;
    private Geometry geom;
    private int priority = 0;
    private float coeff_G = 0.0;
}
