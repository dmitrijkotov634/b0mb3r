from db0mb3r.services.service import Service


class SportmasterUA(Service):
    phone_codes = [380]

    async def run(self):
        await self.get(
            "https://www.sportmaster.ua/",
            params={
                "module": "users",
                "action": "SendSMSReg",
                "phone": self.formatted_phone,
            },
        )
