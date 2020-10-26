from db0mb3r.services.service import Service


class TopShop(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.top-shop.ru/login/loginByPhone/",
            data={"phone": self.format(self.formatted_phone, "+* (***) ***-**-**")},
        )
