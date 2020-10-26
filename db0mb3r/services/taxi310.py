from db0mb3r.services.service import Service


class Taxi310(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "http://62.149.7.19:7200/api/account/register/sendConfirmCode",
            json={"phone": self.phone},
        )
