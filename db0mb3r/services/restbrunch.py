from db0mb3r.services.service import Service


class SushiRolla(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://sushirolla.ru/page/save.php",
            data={
                "send_me_password": 1,
                "phone": self.format(self.formatted_phone, "+*(***) ***-**-**"),
            },
        )
