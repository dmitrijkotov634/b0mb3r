from db0mb3r.services.service import Service


class OkeanSushi(Service):
    phone_codes = [7]

    async def run(self):
        await self.get(
            "https://okeansushi.ru/includes/contact.php",
            params={
                "call_mail": "1",
                "ajax": "1",
                "name": self.russian_name,
                "phone": self.format(self.phone, "8 (***) ***-**-**"),
                "call_time": "1",
                "pravila2": "on",
            },
        )
