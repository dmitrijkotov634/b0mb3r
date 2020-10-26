from db0mb3r.services.service import Service


class PayLate(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://paylate.ru/registry",
            data={
                "mobile": self.format(self.formatted_phone, "+*-***-***--"),
                "first_name": self.russian_name,
                "last_name": self.russian_name,
                "nick_name": self.russian_name,
                "gender-client": 1,
                "email": self.email,
                "action": "registry",
            },
        )
