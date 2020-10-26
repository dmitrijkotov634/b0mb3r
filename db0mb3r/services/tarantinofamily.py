from db0mb3r.services.service import Service


class TarantinoFamily(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
            data={"action": "callback_phonenumber", "phone": self.formatted_phone},
        )
