from db0mb3r.services.service import Service


class Alpari(Service):
    async def run(self):
        await self.post(
            "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": self.email,
                "mobile_phone": self.formatted_phone,
                "deliveryOption": "sms",
            },
        )
