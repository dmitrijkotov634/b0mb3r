from db0mb3r.services.service import Service


class MobilePlanet(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://mobileplanet.ua/register",
            data={
                "klient_name": self.username,
                "klient_phone": "+" + self.formatted_phone,
                "klient_email": self.email,
            },
        )
