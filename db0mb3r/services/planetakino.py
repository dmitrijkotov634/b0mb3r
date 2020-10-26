from db0mb3r.services.service import Service


class PlanetaKino(Service):
    phone_codes = [380]

    async def run(self):
        await self.get(
            "https://cabinet.planetakino.ua/service/sms",
            params={"phone": self.formatted_phone},
        )
