from db0mb3r.services.service import Service


class Moyo(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://www.moyo.ua/identity/registration",
            data={
                "firstname": self.russian_name,
                "phone": self.formatted_phone,
                "email": self.email,
            },
        )
