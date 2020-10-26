from db0mb3r.services.service import Service


class Uchidoma(Service):
    async def run(self):
        await self.post(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + self.formatted_phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            },
        )
        await self.post(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + self.formatted_phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
