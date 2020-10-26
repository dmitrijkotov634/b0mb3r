from db0mb3r.services.service import Service


class KFC(Service):
    async def run(self):
        await self.post(
            "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
            json={"phone": "+" + self.formatted_phone},
        )
