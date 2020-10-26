from db0mb3r.services.service import Service


class CrossStudio(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://cross-studio.ru/ajax/lk/send_sms",
            data={
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "email": self.email,
                "pass": self.password,
                "pass1": self.password,
                "name": self.username,
                "fename": self.username,
                "hash": "",
            },
        )
