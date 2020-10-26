from db0mb3r.services.service import Service


class SushiFuji(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://sushifuji.ru/sms_send_ajax.php",
            data={"name": "false", "phone": self.formatted_phone},
        )
