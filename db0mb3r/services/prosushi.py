from db0mb3r.services.service import Service


class ProSushi(Service):
    async def run(self):
        await self.post(
            "https://www.prosushi.ru/php/profile.php",
            data={"phone": "+" + self.formatted_phone, "mode": "sms"},
        )
