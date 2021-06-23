from db0mb3r.services.service import Service

class Qiwi(Service):

    async def run(self):
        await self.post(
            "https://mobile-api.qiwi.com/oauth/authorize",
            data={"response_type": "urn:qiwi:oauth:response-type:confirmation-id", "username": self.formatted_phone, "client_id": "android-qw", "client_secret": "zAm4FKq9UnSe7id"},
        )