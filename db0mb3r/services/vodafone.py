from db0mb3r.services.service import Service


class Vodafone(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://www.vodafone.ua/shop/ru/vodafone_customer/register/sendSms/",
            data={
                "is_ajax": "true",
                "phone_number": self.format(self.formatted_phone, "+**(***) ***-**-**"),
            },
        )
