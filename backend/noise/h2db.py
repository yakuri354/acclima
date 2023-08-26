from postgis.asyncpg import register
from postgis import Point as PgPt
from . import groovy
from java.sql import ResultSet, DriverManager
from org.h2gis.functions.factory import H2GISFunctions
from typing import Any

# DB_URL = "postgresql://localhost:25432/gis"
# DB_URL = ""

# LIBPQ_URL = f"{DB_URL}?user={secret.DB_USER}&password={secret.DB_PASS}"
# JDBC_URL = f"jdbc:{LIBPQ_URL}"

# def pt2pg(pt: Point) -> PgPt:
# return PgPt(pt.latitude, pt.longitude, srid=OSM_SRID)

# async def get_conn():
# conn = await asyncpg.connect(LIBPQ_URL)
# await register(conn)
# return conn


async def query_all(conn, query: str, params: list[Any] = []) -> list[dict[str, Any]]:
    rs: ResultSet = await exec(conn, query, params)

    md = rs.getMetaData()
    cols = md.getColumnCount()

    data = []

    while rs.next():
        row = dict()
        for i in range(1, cols + 1):
            row[md.getColumnName(i)] = rs.getObject(i)
        data.append(row)

    rs.close()

    return data


async def exec(conn, query: str, params: list[Any] = []) -> ResultSet:
    return await groovy.run_blocking(lambda: exec_bl(conn, query, params))


async def exec_upd(conn, query: str, params: list[Any] = []) -> ResultSet:
    return await groovy.run_blocking(lambda: exec_bl_upd(conn, query, params))


def exec_bl(conn, query: str, params: list[Any] = []) -> ResultSet:
    return exec_fmt(conn, query, params).executeQuery()


def exec_bl_upd(conn, query: str, params: list[Any] = []) -> ResultSet:
    return exec_fmt(conn, query, params).executeUpdate()


def exec_fmt(conn, query: str, params: list[Any] = []):
    pstmt = conn.prepareStatement(query)
    pmd = pstmt.getParameterMetaData()
    for i, param in enumerate(params):
        pstmt.setObject(i + 1, param, pmd.getParameterType(i + 1))
    return pstmt


async def new_h2gis_conn(path):
    conn = await groovy.run_blocking(
        lambda: DriverManager.getConnection(f"jdbc:h2:{path}")
    )
    H2GISFunctions.load(conn)
    return conn
