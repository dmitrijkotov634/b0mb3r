from db0mb3r.services.service import Service


class SushiMaster(Service):
    async def run(self):
        await self.post(
            "https://client-api.sushi-master.ru/api/v1/auth/init",
            json={"phone": self.formatted_phone},
        )
