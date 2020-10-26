from db0mb3r.services.service import Service


class Sayoris(Service):
    async def run(self):
        await self.post(
            "https://sayoris.ru/?route=parse/whats",
            data={"phone": self.formatted_phone},
        )
