from db0mb3r.services.service import Service


class Bluefin(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://bluefin.moscow/auth/register/",
            data={
                "phone": self.format(self.phone, "(***)***-**-**"),
                "sendphone": "Далее",
            },
        )
