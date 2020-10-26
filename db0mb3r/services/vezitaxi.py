from db0mb3r.services.service import Service


class VeziTaxi(Service):
    async def run(self):
        await self.get(
            "https://vezitaxi.com/api/employment/getsmscode",
            params={
                "phone": "+" + self.formatted_phone,
                "city": 561,
                "callback": "jsonp_callback_35979",
            },
        )
