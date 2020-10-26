from db0mb3r.services.service import Service


class Zoopt(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://zoopt.ru/api/",
            data={
                "module": "salin.core",
                "class": r"BonusServer\Auth",
                "action": "SendSms",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
