from db0mb3r.services.service import Service


class EasyPay(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://api.easypay.ua/api/auth/register",
            json={"phone": self.formatted_phone, "password": self.password},
        )
