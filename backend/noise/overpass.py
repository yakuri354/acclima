import textwrap
from aiohttp import ClientSession
from logging import info, debug
from time import time

from .comp import OSM_SRID, Point
from .const import *


def around_point(pt: Point, r: float):
    p2 = pt.with_srid(OSM_SRID)
    way_filter = "\n".join(
        [f"way[{tag}](around:{r},{p2.x},{p2.y});" for tag in OVERPASS_TAGS]
    )
    q = f"""(
        {way_filter}
    );
    out meta;
    >;
    out meta qt;
    """
    return textwrap.dedent(q)


async def overpass_fetch(pt: Point, r: float, file: str, sess: ClientSession):
    query = around_point(pt, r)

    debug("starting overpass fetch")

    st_t = time()

    sz = 0
    async with sess.get(OVERPASS_URL, params={"data": query}) as resp:
        with open(file, "wb") as fd:
            async for chunk in resp.content.iter_any():
                sz += len(chunk)
                fd.write(chunk)

    info(
        "overpass query for {} of size {} mb finished in {:.2f} s",
        pt,
        sz / 1e6,
        time() - st_t,
    )
