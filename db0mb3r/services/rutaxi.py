from db0mb3r.services.service import Service


class RuTaxi(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://rutaxi.ru/ajax_auth.html", data={"l": self.phone, "c": "3"},
        )
