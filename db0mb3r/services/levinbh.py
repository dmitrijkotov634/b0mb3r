from db0mb3r.services.service import Service


class LevinBH(Service):
    async def run(self):
        await self.post(
            "https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",
            json={
                "url": "/api/client/phone_verification",
                "method": "POST",
                "data": {
                    "client_id": 5646981,
                    "phone": self.formatted_phone,
                    "alisa_id": 1,
                },
                "headers": {
                    "Client-Id": 5646981,
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            },
        )
