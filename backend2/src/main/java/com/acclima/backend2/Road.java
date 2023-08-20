package com.acclima.backend2;

import java.math.BigDecimal;

public class Road {
    public Road(org.openstreetmap.osmosis.core.domain.v0_6.Way way) {
        this.way = way;
        this.id = way.getId();
        for (org.openstreetmap.osmosis.core.domain.v0_6.Tag tag : way.getTags()) {
            if ("maxspeed".equalsIgnoreCase(tag.getKey())) {
                try {
                    this.maxspeed = java.lang.Double.parseDouble(tag.getValue().replaceAll("[^0-9]+", ""));
                } catch (java.lang.NumberFormatException e) {
                    // in case maxspeed does not contain a numerical value
                }

                if (tag.getValue().contains("mph")) {
                    maxspeed = maxspeed * 1.60934;
                }

            }

            if ("highway".equalsIgnoreCase(tag.getKey())) {
                this.type = tag.getValue();
            }

            if ("highway".equalsIgnoreCase(tag.getKey()) && "yes".equalsIgnoreCase(tag.getValue())) {
                oneway = true;
            }

        }

        updateCategory();
    }

    public double getNbLV(java.lang.String period) {
        double lv;
        if (period.equals("d")) {
            lv = (1 - hv_d.get(category)) * aadf_d.get(category) / hours_in_d;
        } else if (period.equals("e")) {
            lv = (1 - hv_e.get(category)) * aadf_e.get(category) / hours_in_e;
        } else {// n
            lv = (1 - hv_n.get(category)) * aadf_n.get(category) / hours_in_n;
        }

        if (oneway) {
            lv /= 2;
        }

        return lv;
    }

    public double getNbHV(java.lang.String period) {
        double hv;
        if (period.equals("d")) {
            hv = hv_d.get(category) * new BigDecimal(aadf_d.get(category)) / hours_in_d;
        } else if (period.equals("e")) {
            hv = hv_e.get(category) * aadf_e.get(category) / hours_in_e;
        } else {// n
            hv = hv_n.get(category) * aadf_n.get(category) / hours_in_n;
        }

        if (oneway) {
            hv /= 2;
        }

        return hv;
    }

    public void updateCategory() {
        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("motorway", "motorway_link")).contains(type)) {
            category = 0;
        }

        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("trunk", "trunk_link")).contains(type)) {
            category = 1;
        }

        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("primary", "primary_link")).contains(type)) {
            category = 2;
        }

        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("secondary", "secondary_link")).contains(type)) {
            category = 3;
        }

        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("tertiary", "tertiary_link", "unclassified")).contains(type)) {
            category = 4;
        }

        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("residential")).contains(type)) {
            category = 5;
        }

        if (new java.util.ArrayList<java.lang.String>(java.util.Arrays.asList("service", "living_street")).contains(type)) {
            category = 6;
        }

    }

    public void setGeom(Geometry geom) {
        this.geom = geom;
    }

    public void setHeight(double height) {
        this.setHeight(height);
    }

    public static java.util.ArrayList<java.lang.Integer> getAadf_d() {
        return aadf_d;
    }

    public static void setAadf_d(java.util.ArrayList<java.lang.Integer> aadf_d) {
        Road.aadf_d = aadf_d;
    }

    public static java.util.ArrayList<java.lang.Integer> getAadf_e() {
        return aadf_e;
    }

    public static void setAadf_e(java.util.ArrayList<java.lang.Integer> aadf_e) {
        Road.aadf_e = aadf_e;
    }

    public static java.util.ArrayList<java.lang.Integer> getAadf_n() {
        return aadf_n;
    }

    public static void setAadf_n(java.util.ArrayList<java.lang.Integer> aadf_n) {
        Road.aadf_n = aadf_n;
    }

    public static java.util.ArrayList<java.math.BigDecimal> getHv_d() {
        return hv_d;
    }

    public static void setHv_d(java.util.ArrayList<java.math.BigDecimal> hv_d) {
        Road.hv_d = hv_d;
    }

    public static java.util.ArrayList<java.math.BigDecimal> getHv_e() {
        return hv_e;
    }

    public static void setHv_e(java.util.ArrayList<java.math.BigDecimal> hv_e) {
        Road.hv_e = hv_e;
    }

    public static java.util.ArrayList<java.math.BigDecimal> getHv_n() {
        return hv_n;
    }

    public static void setHv_n(java.util.ArrayList<java.math.BigDecimal> hv_n) {
        Road.hv_n = hv_n;
    }

    public static java.util.ArrayList<java.lang.Integer> getSpeed() {
        return speed;
    }

    public static void setSpeed(java.util.ArrayList<java.lang.Integer> speed) {
        Road.speed = speed;
    }

    public static java.lang.Integer getHours_in_d() {
        return hours_in_d;
    }

    public static void setHours_in_d(java.lang.Integer hours_in_d) {
        Road.hours_in_d = hours_in_d;
    }

    public static java.lang.Integer getHours_in_e() {
        return hours_in_e;
    }

    public static void setHours_in_e(java.lang.Integer hours_in_e) {
        Road.hours_in_e = hours_in_e;
    }

    public static java.lang.Integer getHours_in_n() {
        return hours_in_n;
    }

    public static void setHours_in_n(java.lang.Integer hours_in_n) {
        Road.hours_in_n = hours_in_n;
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

    public double getMaxspeed() {
        return maxspeed;
    }

    public void setMaxspeed(double maxspeed) {
        this.maxspeed = maxspeed;
    }

    public boolean getOneway() {
        return oneway;
    }

    public boolean isOneway() {
        return oneway;
    }

    public void setOneway(boolean oneway) {
        this.oneway = oneway;
    }

    public java.lang.String getType() {
        return type;
    }

    public void setType(java.lang.String type) {
        this.type = type;
    }

    public int getCategory() {
        return category;
    }

    public void setCategory(int category) {
        this.category = category;
    }

    private static java.util.ArrayList<java.lang.Integer> aadf_d = new java.util.ArrayList<java.lang.Integer>(java.util.Arrays.asList(26103, 17936, 7124, 1400, 700, 350, 175));
    private static java.util.ArrayList<java.lang.Integer> aadf_e = new java.util.ArrayList<java.lang.Integer>(java.util.Arrays.asList(7458, 3826, 1069, 400, 200, 100, 50));
    private static java.util.ArrayList<java.lang.Integer> aadf_n = new java.util.ArrayList<java.lang.Integer>(java.util.Arrays.asList(3729, 2152, 712, 200, 100, 50, 25));
    private static java.util.ArrayList<java.math.BigDecimal> hv_d = new java.util.ArrayList<java.math.BigDecimal>(java.util.Arrays.asList(0.25, 0.2, 0.2, 0.15, 0.10, 0.05, 0.02));
    private static java.util.ArrayList<java.math.BigDecimal> hv_e = new java.util.ArrayList<java.math.BigDecimal>(java.util.Arrays.asList(0.35, 0.2, 0.15, 0.10, 0.06, 0.02, 0.01));
    private static java.util.ArrayList<java.math.BigDecimal> hv_n = new java.util.ArrayList<java.math.BigDecimal>(java.util.Arrays.asList(0.45, 0.2, 0.1, 0.05, 0.03, 0.01, 0.0));
    private static java.util.ArrayList<java.lang.Integer> speed = new java.util.ArrayList<java.lang.Integer>(java.util.Arrays.asList(130, 110, 80, 80, 50, 30, 30));
    private static java.lang.Integer hours_in_d = 12;
    private static java.lang.Integer hours_in_e = 4;
    private static java.lang.Integer hours_in_n = 8;
    private long id;
    private org.openstreetmap.osmosis.core.domain.v0_6.Way way;
    private Geometry geom;
    private double maxspeed = 0.0;
    private boolean oneway = false;
    private java.lang.String type = null;
    private int category = 5;
}
