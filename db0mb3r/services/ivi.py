from db0mb3r.services.service import Service


class IVI(Service):
    async def run(self):
        await self.post(
            "https://api.ivi.ru/mobileapi/user/register/phone/v6",
            data={"phone": self.formatted_phone},
        )
