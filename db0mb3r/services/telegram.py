from db0mb3r.services.service import Service

class Telegram(Service):

    async def run(self):
        await self.post(
            "https://my.telegram.org/auth/send_password",
            data={'phone': '+' + self.formatted_phone},
        )
