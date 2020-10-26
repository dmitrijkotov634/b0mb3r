from db0mb3r.services.service import Service


class Karusel(Service):
    async def run(self):
        await self.post(
            "https://app.karusel.ru/api/v1/phone/", data={"phone": self.formatted_phone}
        )
