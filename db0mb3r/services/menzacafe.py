from db0mb3r.services.service import Service


class MenzaCafe(Service):
    phone_codes = [7]

    async def run(self):
        await self.get(
            "https://menza-cafe.ru/system/call_me.php",
            params={
                "fio": self.russian_name,
                "phone": self.formatted_phone,
                "phone_number": "1",
            },
        )
