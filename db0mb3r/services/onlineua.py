from db0mb3r.services.service import Service


class OnlineUa(Service):
    phone_codes = [380]

    async def run(self):
        await self.get(
            "https://secure.online.ua/ajax/check_phone/",
            params={"reg_phone": self.phone},
        )
