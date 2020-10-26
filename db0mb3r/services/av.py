from db0mb3r.services.service import Service


class AzbukaVkusa(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://oauth.av.ru/check-phone",
            json={"phone": self.format(self.formatted_phone, "+* (***) ***-**-**")},
        )
