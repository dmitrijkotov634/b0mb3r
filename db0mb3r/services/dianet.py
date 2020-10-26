from db0mb3r.services.service import Service


class Dianet(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://my.dianet.com.ua/send_sms/", data={"phone": self.phone},
        )
