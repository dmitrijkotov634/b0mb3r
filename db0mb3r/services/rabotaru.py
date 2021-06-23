from db0mb3r.services.service import Service

class RabotaRu(Service):

    async def run(self):
        await self.post(
            "https://www.rabota.ru/remind",
            data={"credential": self.formatted_phone},
        )
