from db0mb3r.services.service import Service


class Kyivstar(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://cas-api.kyivstar.ua/api/sendSms",
            data={"lang": "uk", "msisdn": self.formatted_phone},
        )
