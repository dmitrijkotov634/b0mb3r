from db0mb3r.services.service import Service


class Taxi3040(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://3040.com.ua/taxi-ordering",
            data={"callback-phone": self.formatted_phone},
        )
