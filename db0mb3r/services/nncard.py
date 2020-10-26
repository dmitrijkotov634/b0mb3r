from db0mb3r.services.service import Service


class NNCard(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://nn-card.ru/api/1.0/register",
            json={"phone": self.formatted_phone, "password": self.password},
        )
