import jpype
import os.path
import asyncio
from os import cpu_count
import concurrent.futures
import jpype.imports
from jpype.types import *

if not jpype.isJVMStarted(): # type: ignore
    jpype.startJVM(classpath=[os.path.abspath(x) for x in ['java_lib/*', 'noisemodelling_dist/lib/*']]) # type: ignore

from java.io import File
from java.util import HashMap

# invoke classloader
JClass("org.h2.Driver")

GroovyShell = JClass("groovy.lang.GroovyShell")

shell = GroovyShell()

executor = concurrent.futures.ThreadPoolExecutor(cpu_count(), "acclima_wrk_")

async def run_blocking(f):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, f)

# TODO maybe make it less ugly?
# TODO PostGIS
async def invoke(path: str, conn, input: dict):
    script = await run_blocking(lambda: shell.parse(File('noisemodelling_dist/noisemodelling/wps/' + (path if path.endswith(".groovy") else path + ".groovy"))))
    # conn = await run_blocking(lambda: DriverManager.getConnection(db.JDBC_URL))
    try:
        return await run_blocking(lambda: script.invokeMethod("exec", JObject[:]([conn, HashMap(input)]))) # type: ignore
    finally:
        await run_blocking(lambda: conn.close())
