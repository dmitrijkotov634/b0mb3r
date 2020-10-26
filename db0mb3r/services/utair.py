from db0mb3r.services.service import Service


class Utair(Service):
    async def run(self):
        await self.post(
            "https://b.utair.ru/api/v1/login/",
            data={"login": "+" + self.formatted_phone},
        )
