from db0mb3r.services.service import Service


class Kaspi(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://kaspi.kz/util/send-app-link", data={"address": self.phone},
        )
