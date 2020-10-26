from db0mb3r.services.service import Service


class Tinkoff(Service):
    async def run(self):
        await self.post(
            "https://api.tinkoff.ru/v1/sign_up",
            data={"phone": "+" + self.formatted_phone},
        )
