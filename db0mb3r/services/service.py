import random
import re
import string
from abc import ABC, abstractmethod
from typing import Callable

import httpx
from loguru import logger
from random_user_agent.user_agent import UserAgent


class Service(ABC):
    user_agent_rotator = UserAgent()
    headers = {
        "User-Agent": user_agent_rotator.get_random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
    }
    country_codes = {"7": "ru", "375": "by", "380": "ua"}
    phone_codes = []
    client = httpx.AsyncClient(headers=headers, verify=False)

    def __init__(self, phone: str, country_code: int):
        self.country_code = str(country_code)
        self.phone = phone[len(self.country_code) :]
        self.formatted_phone = phone

        self.russian_name = "".join(
            random.choice(
                "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
            )
            for _ in range(5)
        )
        self.username = self.password = "".join(
            random.choice(string.ascii_letters) for _ in range(12)
        )
        self.email = (
            f"{self.username}@{random.choice(['gmail.com', 'mail.ru', 'yandex.ru'])}"
        )

    async def get(self, *args, **kwargs):
        return await self.request_logger(self.client.get, *args, **kwargs)

    async def post(self, *args, **kwargs):
        return await self.request_logger(self.client.post, *args, **kwargs)

    async def options(self, *args, **kwargs):
        return await self.request_logger(self.client.options, *args, **kwargs)

    async def request_logger(self, function: Callable, *args, **kwargs):
        response = await function(*args, **kwargs, timeout=3)
        if response.is_error:
            logger.info(
                f"{self.__class__.__name__} returned an error HTTP code: {response.status_code}"
            )

        return response

    async def get_csrf_token(self, url: str, pattern):
        response = await self.get(url)
        return re.search(pattern, response.text).group(1).strip()

    @staticmethod
    def format(phone: str, mask: str, mask_symbol: str = "*"):
        if len(phone) == mask.count(mask_symbol):
            formatted_phone = ""
            for symbol in mask:
                if symbol == mask_symbol:
                    formatted_phone += phone[0]
                    phone = phone[(len(phone) - 1) * -1 :]
                else:
                    formatted_phone += symbol
        else:
            formatted_phone = phone
        return formatted_phone

    @abstractmethod
    async def run(self):
        raise NotImplementedError
