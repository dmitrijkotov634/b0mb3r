from db0mb3r.services.service import Service


class Grillnica(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://grilnica.ru/loginphone/",
            data={
                "step": 0,
                "phone": self.format(self.formatted_phone, "+* (***) ***-****"),
                "code": "",
                "allow_sms": "on",
                "apply_offer": "on",
            },
        )
