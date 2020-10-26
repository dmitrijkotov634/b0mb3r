from db0mb3r.services.service import Service


class FoodBand(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://foodband.ru/api?call=calls",
            data={
                "customerName": self.russian_name,
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "g-recaptcha-response": "",
            },
        )
        await self.get(
            "https://foodband.ru/api/",
            params={
                "call": "customers/sendVerificationCode",
                "phone": self.phone,
                "g-recaptcha-response": "",
            },
        )
