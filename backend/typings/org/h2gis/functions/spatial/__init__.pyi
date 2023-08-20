
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.functions.spatial.affine_transformations
import org.h2gis.functions.spatial.aggregate
import org.h2gis.functions.spatial.buffer
import org.h2gis.functions.spatial.clean
import org.h2gis.functions.spatial.convert
import org.h2gis.functions.spatial.create
import org.h2gis.functions.spatial.crs
import org.h2gis.functions.spatial.distance
import org.h2gis.functions.spatial.earth
import org.h2gis.functions.spatial.edit
import org.h2gis.functions.spatial.generalize
import org.h2gis.functions.spatial.mesh
import org.h2gis.functions.spatial.metadata
import org.h2gis.functions.spatial.operators
import org.h2gis.functions.spatial.predicates
import org.h2gis.functions.spatial.properties
import org.h2gis.functions.spatial.snap
import org.h2gis.functions.spatial.split
import org.h2gis.functions.spatial.topography
import org.h2gis.functions.spatial.topology
import org.h2gis.functions.spatial.trigonometry
import org.h2gis.functions.spatial.volume
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial")``.

    affine_transformations: org.h2gis.functions.spatial.affine_transformations.__module_protocol__
    aggregate: org.h2gis.functions.spatial.aggregate.__module_protocol__
    buffer: org.h2gis.functions.spatial.buffer.__module_protocol__
    clean: org.h2gis.functions.spatial.clean.__module_protocol__
    convert: org.h2gis.functions.spatial.convert.__module_protocol__
    create: org.h2gis.functions.spatial.create.__module_protocol__
    crs: org.h2gis.functions.spatial.crs.__module_protocol__
    distance: org.h2gis.functions.spatial.distance.__module_protocol__
    earth: org.h2gis.functions.spatial.earth.__module_protocol__
    edit: org.h2gis.functions.spatial.edit.__module_protocol__
    generalize: org.h2gis.functions.spatial.generalize.__module_protocol__
    mesh: org.h2gis.functions.spatial.mesh.__module_protocol__
    metadata: org.h2gis.functions.spatial.metadata.__module_protocol__
    operators: org.h2gis.functions.spatial.operators.__module_protocol__
    predicates: org.h2gis.functions.spatial.predicates.__module_protocol__
    properties: org.h2gis.functions.spatial.properties.__module_protocol__
    snap: org.h2gis.functions.spatial.snap.__module_protocol__
    split: org.h2gis.functions.spatial.split.__module_protocol__
    topography: org.h2gis.functions.spatial.topography.__module_protocol__
    topology: org.h2gis.functions.spatial.topology.__module_protocol__
    trigonometry: org.h2gis.functions.spatial.trigonometry.__module_protocol__
    volume: org.h2gis.functions.spatial.volume.__module_protocol__
