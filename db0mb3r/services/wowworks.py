from db0mb3r.services.service import Service


class WowWorks(Service):
    async def run(self):
        await self.post(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": self.formatted_phone, "type": 2},
        )
