from db0mb3r.services.service import Service


class Tabasko(Service):
    async def run(self):
        await self.post(
            "https://tabasko.su/",
            data={
                "IS_AJAX": "Y",
                "COMPONENT_NAME": "AUTH",
                "ACTION": "GET_CODE",
                "LOGIN": self.formatted_phone,
            },
        )
