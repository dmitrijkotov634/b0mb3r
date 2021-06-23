import asyncio
import os
import re
import subprocess
import sys
import webbrowser
from functools import lru_cache
from typing import Awaitable, Callable

import pkg_resources
import httpx

from loguru import logger

@logger.catch
def open_url(url: str):
    logger.info(f"Opening {url}...")
    if "com.termux" in os.environ.get("PREFIX", ""):  # If device is running Termux
        try:
            subprocess.run(
                [
                    "am",
                    "start",
                    "--user",
                    "0",
                    "-a",
                    "android.intent.action.VIEW",
                    "-d",
                    url,
                ]
            )
            return
        except FileNotFoundError:
            pass

    webbrowser.open(url, new=2, autoraise=True)


@logger.catch
@lru_cache(maxsize=None)
def retrieve_installed_version() -> str:
    package_info = subprocess.run(
        [sys.executable, "-m", "pip", "show", "db0mb3r"],
        stdout=subprocess.PIPE,
        check=True,
    )
    bytes_version = re.search(br"Version: ([0-9]\.[0-9.]*)", package_info.stdout).group(
        1
    )
    return bytes_version.decode()

@logger.catch
def check_and_upgrade():
    logger.info("Checking for updates")

    version = pkg_resources.get_distribution("db0mb3r").version
    updates = httpx.get("https://raw.githubusercontent.com/dmitrijkotov634/b0mb3r/master/version")

    if updates.status_code == 200:
        values = updates.text[1:].split("\r\n", maxsplit=1)

        if version == values[0]:
            logger.success("No update required")
        else:
            logger.info("Downloading an update using pip")

            subprocess.check_call([sys.executable, "-m", "pip", "install", "db0mb3r==" + values[0]])
            logger.success("db0mb3r updated, changes will take effect after restart")

            print("\nChanges {}:\n{}\n".format(*values))          
            os.chdir(os.path.join(pkg_resources.get_distribution("db0mb3r").location, "db0mb3r"))

@logger.catch
async def await_with_callback(
    coroutine: Awaitable, callback: Callable, *args, **kwargs
):
    try:
        await coroutine
    except asyncio.CancelledError:
        raise
    except Exception:
        pass
    finally:
        callback(*args, **kwargs)
