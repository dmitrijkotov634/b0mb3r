from db0mb3r.services.service import Service


class Oldi(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.oldi.ru/ajax/reg.php",
            data={
                "method": "isUserPhone",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
