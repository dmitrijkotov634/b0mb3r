import asyncio
import os
import sys

import click
import pkg_resources
import uvicorn
from loguru import logger

os.chdir(os.path.join(pkg_resources.get_distribution("db0mb3r").location, "db0mb3r"))

from db0mb3r.app.main import app
from db0mb3r.service import prepare_services
from db0mb3r.utils import open_url

from requests import get
import pip

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
        try:
            logger.info("Checking for updates")
            version = pkg_resources.get_distribution("db0mb3r").version
            updates = get("http://dmitry.darkhost.pro/db0mb3r.version", timeout=7)
            if updates.status_code == 200:
                values = updates.text.split("\n", maxsplit=1)
                if version == values[0]:
                    logger.success("No update required")
                else:
                    logger.info("Downloading an update using pip")
                    pip.main(["install", "--upgrade", "db0mb3r==" + values[0]])
                    logger.success("db0mb3r updated, changes will take effect after restart")
                    print("\nChanges {}:\n{}\n".format(*values))          
                    os.chdir(os.path.join(pkg_resources.get_distribution("db0mb3r").location, "db0mb3r"))
            else:
                logger.error("db0mb3r service could not provide the latest version")
        except:
            logger.error("Failed to check the latest updates")

    prepare_services()

    if not only_api:
        open_url(f"http://{ip}:{port}/")

    uvicorn.run(app, host=ip, port=port, log_level="error")


main()
