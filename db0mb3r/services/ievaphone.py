from db0mb3r.services.service import Service


class IevaPhone(Service):
    async def run(self):
        await self.get(
            "https://ievaphone.com/call-my-phone/web/request-free-call",
            params={
                "phone": self.formatted_phone,
                "domain": "IEVAPHONE",
                "browser": "undefined",
            },
        )
