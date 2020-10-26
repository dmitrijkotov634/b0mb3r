from db0mb3r.services.service import Service


class QBBox(Service):
    async def run(self):
        await self.post(
            "https://qbbox.ru/api/user",
            json={"phone": self.formatted_phone, "account_type": 1},
        )
