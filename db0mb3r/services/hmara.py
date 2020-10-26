from db0mb3r.services.service import Service


class Hmara(Service):
    async def run(self):
        await self.get(
            "https://api.hmara.tv/stable/entrance",
            params={"contact": self.formatted_phone},
        )
