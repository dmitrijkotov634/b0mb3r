from db0mb3r.services.service import Service


class MyGames(Service):
    async def run(self):
        await self.post(
            "https://account.my.games/signup_send_sms/",
            data={"phone": self.formatted_phone},
        )
