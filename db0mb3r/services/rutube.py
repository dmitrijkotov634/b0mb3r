from db0mb3r.services.service import Service


class RuTube(Service):
    async def run(self):
        await self.post(
            "https://pass.rutube.ru/api/accounts/phone/send-password/",
            json={"phone": "+" + self.formatted_phone},
        )
