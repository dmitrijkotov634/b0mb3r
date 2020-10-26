from db0mb3r.services.service import Service


class VisaPay(Service):
    async def run(self):
        await self.post(
            "https://pay.visa.ru/api/Auth/code/request",
            json={"phoneNumber": "+" + self.formatted_phone},
        )
