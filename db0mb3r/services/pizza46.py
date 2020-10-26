from db0mb3r.services.service import Service


class Pizza46(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://pizza46.ru/ajaxGet.php",
            data={"phone": self.format(self.formatted_phone, "+* (***) ***-****")},
        )
