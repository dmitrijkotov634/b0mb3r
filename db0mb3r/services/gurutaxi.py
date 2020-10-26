from db0mb3r.services.service import Service


class GuruTaxi(Service):
    async def run(self):
        await self.post(
            "https://guru.taxi/api/v1/driver/session/verify",
            json={"phone": {"code": 1, "number": self.phone}},
        )
