from db0mb3r.services.service import Service


class VSK(Service):
    async def run(self):
        await self.post(
            "https://shop.vsk.ru/ajax/auth/postSms/",
            data={"phone": self.formatted_phone},
        )
