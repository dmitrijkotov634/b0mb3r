from db0mb3r.services.service import Service


class OnTaxi(Service):
    async def run(self):
        if self.country_code in self.country_codes:
            await self.post(
                "https://ontaxi.com.ua/api/v2/web/client",
                json={
                    "country": self.country_codes[self.country_code].upper(),
                    "phone": self.phone,
                },
            )
