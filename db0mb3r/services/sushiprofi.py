from db0mb3r.services.service import Service


class SushiProfi(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.sushi-profi.ru/api/order/order-call/",
            json={"phone": self.phone, "name": self.russian_name},
        )
