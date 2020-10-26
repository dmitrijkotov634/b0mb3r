from db0mb3r.services.service import Service


class Citilink(Service):
    async def run(self):
        await self.post(
            f"https://www.citilink.ru/registration/confirm/phone/+{self.formatted_phone}/"
        )
