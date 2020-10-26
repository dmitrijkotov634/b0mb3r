from db0mb3r.services.service import Service


class MonoBank(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": "+" + self.formatted_phone},
        )
