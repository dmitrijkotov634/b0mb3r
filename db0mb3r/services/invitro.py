from db0mb3r.services.service import Service


class Invitro(Service):
    async def run(self):
        await self.post(
            "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
            data={
                "password": self.password,
                "application": "lkp",
                "login": "+" + self.formatted_phone,
            },
        )
