from db0mb3r.services.service import Service


class Creditter(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://api.creditter.ru/confirm/sms/send",
            json={
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "type": "register",
            },
        )
