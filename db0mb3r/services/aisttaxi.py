from db0mb3r.services.service import Service


class AistTaxi(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "http://94.154.218.82:7201/api/account/register/sendConfirmCode",
            json={"phone": self.phone},
        )
