from db0mb3r.services.service import Service


class WifiMetro(Service):
    async def run(self):
        await self.post(
            "https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": self.formatted_phone},
            headers={"App-ID": "cabinet"},
        )
