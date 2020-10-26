from db0mb3r.services.service import Service


class StarPizzaCafe(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://pizzasushiwok.ru/index.php",
            data={
                "aj": "50",
                "registration-phone": self.format(
                    self.formatted_phone, "+** (***) ***-**-**"
                ),
            },
        )
