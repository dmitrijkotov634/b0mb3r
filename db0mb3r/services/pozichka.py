from db0mb3r.services.service import Service


class Pozichka(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://api.pozichka.ua/v1/registration/send",
            json={
                "RegisterSendForm": {
                    "phone": self.format(self.formatted_phone, "+**-***-***-**-**")
                }
            },
        )
