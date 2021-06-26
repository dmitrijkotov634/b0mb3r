from db0mb3r.services.service import Service

class Kari(Service):

    async def run(self):
        await self.get(
            "https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B" + self.formatted_phone
        )