from db0mb3r.services.service import Service


class PizzaSinizza(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://pizzasinizza.ru/api/phoneCode.php", json={"phone": self.phone},
        )
