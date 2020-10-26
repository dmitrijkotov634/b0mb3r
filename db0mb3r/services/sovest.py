from db0mb3r.services.service import Service


class Sovest(Service):
    async def run(self):
        await self.get(
            "https://oauth.sovest.ru/oauth/authorize",
            data={
                "client_id": "dbo_web",
                "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                "username": "+" + self.formatted_phone,
                "recaptcha": "",
            },
        )
