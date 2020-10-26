from db0mb3r.services.service import Service


class FriendsClub(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + self.formatted_phone},
        )
