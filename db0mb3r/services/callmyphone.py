from db0mb3r.services.service import Service


class CallMyPhone(Service):
    async def run(self):
        await self.post(
            "https://callmyphone.org/do-call",
            data={"phone": "+" + self.formatted_phone, "browser": "undefined"},
        )
