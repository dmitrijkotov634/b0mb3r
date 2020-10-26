from db0mb3r.services.service import Service


class FixPrice(Service):
    async def run(self):
        await self.post(
            "https://fix-price.ru/ajax/register_phone_code.php",
            data={
                "register_call": "Y",
                "action": "getCode",
                "phone": "+" + self.formatted_phone,
            },
        )
