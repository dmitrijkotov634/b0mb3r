from db0mb3r.services.service import Service


class Kant(Service):
    async def run(self):
        await self.post(
            "https://www.kant.ru/ajax/profile/send_authcode.php",
            data={"Phone": self.formatted_phone},
        )
