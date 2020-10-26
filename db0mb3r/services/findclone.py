from db0mb3r.services.service import Service


class FindClone(Service):
    async def run(self):
        await self.get(
            "https://findclone.ru/register",
            params={"phone": "+" + self.formatted_phone},
        )
