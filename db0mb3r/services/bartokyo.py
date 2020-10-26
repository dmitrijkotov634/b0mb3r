from db0mb3r.services.service import Service


class Bartokyo(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://bartokyo.ru/ajax/login.php",
            data={
                "user_phone": self.format(self.formatted_phone, "+* (***) ***-****"),
            },
        )
