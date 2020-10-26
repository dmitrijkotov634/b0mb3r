from db0mb3r.services.service import Service


class Helsi(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://helsi.me/api/healthy/accounts/login",
            json={"phone": self.formatted_phone, "platform": "PISWeb"},
        )
