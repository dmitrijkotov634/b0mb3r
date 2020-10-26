from db0mb3r.services.service import Service


class Thehive(Service):
    async def run(self):
        await self.post(
            "https://thehive.pro/auth/signup",
            json={"phone": "+" + self.formatted_phone},
        )
