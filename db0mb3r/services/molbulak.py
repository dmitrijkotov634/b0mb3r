from db0mb3r.services.service import Service


class Molbulak(Service):
    async def run(self):
        await self.post(
            "https://www.molbulak.ru/ajax/smsservice.php",
            data={"command": "send_code_loan", "phone": "+" + self.formatted_phone},
        )
