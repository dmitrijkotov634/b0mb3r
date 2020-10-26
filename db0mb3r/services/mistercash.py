from db0mb3r.services.service import Service


class MisterCash(Service):
    phone_codes = [380]

    async def run(self):
        await self.get(
            "https://my.mistercash.ua/ru/send/sms/registration",
            params={"number": "+" + self.formatted_phone},
        )
