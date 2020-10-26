from db0mb3r.services.service import Service


class Benzuber(Service):
    async def run(self):
        await self.post(
            "https://app.benzuber.ru/login", data={"phone": "+" + self.formatted_phone},
        )
