from db0mb3r.services.service import Service


class RendesVouz(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",
            data={
                "phone": self.format(self.formatted_phone, "+*(***)***-**-**"),
                "alien": "0",
            },
        )
