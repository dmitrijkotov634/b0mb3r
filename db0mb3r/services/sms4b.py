from db0mb3r.services.service import Service


class SMS4b(Service):
    async def run(self):
        await self.post(
            "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + self.formatted_phone, "ajax_demo_send": "1"},
        )
