from db0mb3r.services.service import Service


class Sedi(Service):
    phone_codes = [7]

    async def run(self):
        await self.get(
            "https://msk1.sedi.ru/webapi",
            params={
                "callback": "jQuery19107992940218113256_1595059640271",
                "q": "get_activation_key",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "way": "bysms",
                "usertype": "customer",
                "lang": "ru-RU",
                "apikey": "EF96ADBE-2DFC-48F7-AF0A-69A007223039",
            },
        )
