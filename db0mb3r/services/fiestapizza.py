from db0mb3r.services.service import Service


class FiestaPizza(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://2407.smartomato.ru/account/session",
            json={
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "g-recaptcha-response": None,
            },
        )
