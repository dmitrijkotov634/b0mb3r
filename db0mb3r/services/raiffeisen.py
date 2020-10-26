from db0mb3r.services.service import Service


class Raiffeisen(Service):
    async def run(self):
        await self.get(
            "https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": self.formatted_phone},
        )
