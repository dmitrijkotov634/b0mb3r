from db0mb3r.services.service import Service


class ChefMarket(Service):
    async def run(self):
        await self.get(
            "https://cm2api.chefmarket.ru/api/v1/clients/request-pin",
            json={"phone": self.formatted_phone},
            headers={"Platform-ID": "webDesktop"},
        )
