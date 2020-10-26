from db0mb3r.services.service import Service


class Call2Friends(Service):
    async def run(self):
        await self.get(
            "https://call2friends.com/call-my-phone/web/request-free-call",
            params={
                "phone": self.formatted_phone,
                "domain": "CALL2FRIENDS",
                "browser": "undefined",
            },
        )
