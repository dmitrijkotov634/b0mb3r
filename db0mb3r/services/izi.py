from db0mb3r.services.service import Service


class IziUA(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://izi.ua/api/auth/register",
            json={
                "phone": "+" + self.formatted_phone,
                "name": self.russian_name,
                "is_terms_accepted": True,
            },
        )
        await self.post(
            "https://izi.ua/api/auth/sms-login",
            json={"phone": "+" + self.formatted_phone},
        )
