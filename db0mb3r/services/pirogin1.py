from db0mb3r.services.service import Service


class PirogiN1(Service):
    async def run(self):
        await self.post(
            "https://piroginomerodin.ru/index.php?route=sms/login/sendreg",
            data={"telephone": "+" + self.formatted_phone},
        )
