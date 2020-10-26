from db0mb3r.services.service import Service


class RichFamily(Service):
    async def run(self):
        await self.post(
            "https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",
            data={"phone": "+" + self.formatted_phone},
        )
