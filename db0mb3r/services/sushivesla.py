from db0mb3r.services.service import Service


class SushiVesla(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://xn--80adjkr6adm9b.xn--p1ai/api/v5/user/start-authorization",
            json={"phone": self.format(self.formatted_phone, "+* *** ***-**-**")},
        )
