from db0mb3r.services.service import Service


class MakiMaki(Service):
    phone_codes = [7]

    async def run(self):
        await self.get(
            "https://makimaki.ru/system/callback.php",
            params={
                "cb_fio": self.russian_name,
                "cb_phone": self.format(self.formatted_phone, "+* *** *** ** **"),
            },
        )
