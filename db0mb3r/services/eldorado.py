from db0mb3r.services.service import Service


class EldoradoUA(Service):
    phone_codes = [380]

    async def run(self):
        await self.get(
            "https://api.eldorado.ua/v1/sign/",
            params={
                "login": self.formatted_phone,
                "step": "phone-check",
                "fb_id": "null",
                "fb_token": "null",
                "lang": "ru",
            },
        )
