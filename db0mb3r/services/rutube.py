from db0mb3r.services.service import Service

class Rutube(Service):

    async def run(self):
        await self.post(
            "https://rutube.ru/api/accounts/sendpass/phone",
            data={"phone": "+" + self.formatted_phone}
        )