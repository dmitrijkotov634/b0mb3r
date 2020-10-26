from db0mb3r.services.service import Service


class MosPizza(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",
            data={"name": self.russian_name, "phone": self.formatted_phone},
        )
