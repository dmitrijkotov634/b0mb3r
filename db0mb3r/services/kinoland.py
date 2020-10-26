from db0mb3r.services.service import Service


class Kinoland(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://api.kinoland.com.ua/api/v1/service/send-sms",
            headers={"Agent": "website"},
            json={"Phone": self.formatted_phone, "Type": 1},
        )
