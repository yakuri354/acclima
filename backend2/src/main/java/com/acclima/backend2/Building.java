public class Building {
    public Building(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        this.way = way;
        this.id = way.getId();
        double h = 4.0 + rand.invokeMethod("nextDouble", new java.lang.Object[0]) * 2.1;
        boolean trueHeightFound = false;
        for (org.openstreetmap.osmosis.core.domain.v0_6.Tag tag : way.getTags()) {
            if (!trueHeightFound && "building:levels".equalsIgnoreCase(tag.getKey())) {
                h = h - 4 + java.lang.Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", "")) * 3.0;
            }

            if ("height".equalsIgnoreCase(tag.getKey())) {
                h = java.lang.Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", ""));
                trueHeightFound = true;
            }

        }

        this.height = h;
    }

    public Building(org.openstreetmap.osmosis.core.domain.v0_6.Way way, double height) {
        this.way = way;
        this.id = way.getId();
        this.height = height;
    }

    public void setGeom(Geometry geom) {
        this.geom = geom;
    }

    public void setHeight(double height) {
        this.height = height;
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

    public double getHeight() {
        return height;
    }

    private long id;
    private org.openstreetmap.osmosis.core.domain.v0_6.Way way;
    private Geometry geom;
    private double height = 0.0;
}
