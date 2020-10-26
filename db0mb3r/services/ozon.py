from db0mb3r.services.service import Service


class Ozon(Service):
    async def run(self):
        await self.post(
            "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": self.formatted_phone, "otpId": 0},
        )
