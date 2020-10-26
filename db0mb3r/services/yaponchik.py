from db0mb3r.services.service import Service


class Yaponchik(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://yaponchik.net/login/login.php",
            data={
                "login": "Y",
                "countdown": 0,
                "step": "phone",
                "redirect": "/profile/",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
