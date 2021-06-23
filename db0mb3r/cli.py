import asyncio
import os
import sys

import click
import pkg_resources
import uvicorn
import subprocess

from loguru import logger

os.chdir(os.path.join(pkg_resources.get_distribution("db0mb3r").location, "db0mb3r"))

from db0mb3r.app.main import app
from db0mb3r.service import prepare_services
from db0mb3r.utils import open_url, check_and_upgrade

@logger.catch
@click.command()
@click.option("--ip", default="127.0.0.1")
@click.option("--port", default=8080)
@click.option("--only-api", "only_api", is_flag=True, default=False)
@click.option("--disable-updates", "disable_updates", is_flag=True, default=False)
def main(ip: str, port: int, only_api: bool = False, disable_updates: bool = False):
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    app.state.only_api = only_api
    
    if not disable_updates:
        check_and_upgrade()

    prepare_services()

    if not only_api:
        open_url(f"http://{ip}:{port}/")

    uvicorn.run(app, host=ip, port=port, log_level="error")

main()
