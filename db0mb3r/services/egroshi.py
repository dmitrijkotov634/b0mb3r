from db0mb3r.services.service import Service


class EGroshi(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://e-groshi.com/online/reg",
            data={
                "first_name": self.username,
                "last_name": self.username,
                "third_name": self.username,
                "phone": self.format(self.formatted_phone, "+** (***) ***-**-**"),
                "password": self.password,
                "password2": self.password,
            },
        )
