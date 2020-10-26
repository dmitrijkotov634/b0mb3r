from db0mb3r.services.service import Service


class Worki(Service):
    async def run(self):
        await self.post(
            "https://api.iconjob.co/api/auth/verification_code",
            json={"phone": self.formatted_phone},
        )
