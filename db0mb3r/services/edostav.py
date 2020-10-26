from db0mb3r.services.service import Service


class Edostav(Service):
    async def run(self):
        await self.post(
            "https://vladimir.edostav.ru/site/CheckAuthLogin",
            data={"phone_or_email": "+" + self.formatted_phone},
        )
