from db0mb3r.services.service import Service


class Sportmaster(Service):
    phone_codes = [7]

    async def run(self):
        await self.get(
            "https://www.sportmaster.ru/user/session/sendSmsCode.do",
            params={"phone": self.format(self.formatted_phone, "+* (***) ***-**-**")},
        )
