from db0mb3r.services.service import Service


class Suanshi(Service):
    async def run(self):
        await self.get(
            "https://suandshi.ru/mobile_api/register_mobile_user",
            params={"phone": self.formatted_phone},
        )
