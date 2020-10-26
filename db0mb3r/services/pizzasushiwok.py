from db0mb3r.services.service import Service


class PizzaSushiWok(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://pizzasushiwok.ru/index.php",
            data={
                "mod_name": "call_me",
                "task": "request_call",
                "name": self.russian_name,
                "phone": self.format(self.formatted_phone, "8-***-***-**-**"),
            },
        )
