from db0mb3r.services.service import Service


class Imgur(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": self.formatted_phone, "region_code": "RU"},
        )
