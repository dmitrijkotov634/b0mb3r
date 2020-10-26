from db0mb3r.services.service import Service


class UlybkaRadugi(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.r-ulybka.ru/login/ajax.php",
            data={
                "action": "sendcode",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
