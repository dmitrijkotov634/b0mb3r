from db0mb3r.services.service import Service


class InDriver(Service):
    async def run(self):
        await self.post(
            "https://terra-1.indriverapp.com/api/authorization?locale=ru",
            data={
                "mode": "request",
                "phone": "+" + self.formatted_phone,
                "phone_permission": "unknown",
                "stream_id": 0,
                "v": 3,
                "appversion": "3.20.6",
                "osversion": "unknown",
                "devicemodel": "unknown",
            },
        )
