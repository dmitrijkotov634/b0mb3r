from db0mb3r.services.service import Service


class Boosty(Service):
    async def run(self):
        await self.post(
            "https://api.boosty.to/oauth/phone/authorize",
            data={"client_id": "+" + self.formatted_phone},
        )
