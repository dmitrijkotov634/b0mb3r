from db0mb3r.services.service import Service


class Multiplex(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://auth.multiplex.ua/login", json={"login": self.formatted_phone},
        )
