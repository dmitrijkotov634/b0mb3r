from db0mb3r.services.service import Service


class Tabris(Service):
    async def run(self):
        await self.post(
            "https://lk.tabris.ru/reg/",
            data={"action": "phone", "phone": self.formatted_phone},
        )
