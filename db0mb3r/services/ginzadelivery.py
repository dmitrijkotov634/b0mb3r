from db0mb3r.services.service import Service


class Kant(Service):
    async def run(self):
        await self.post(
            "https://ginzadelivery.ru/v1/auth", json={"phone": self.formatted_phone},
        )
