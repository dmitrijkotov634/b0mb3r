from db0mb3r.services.service import Service


class Tele2(Service):
    async def run(self):
        await self.post(
            "https://msk.tele2.ru/api/validation/number/" + self.formatted_phone,
            json={"sender": "Tele2"},
        )
