from db0mb3r.services.service import Service


class PizzaKazan(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://pizzakazan.com/auth/ajax.php",
            data={"phone": "+" + self.formatted_phone, "method": "sendCode"},
        )
