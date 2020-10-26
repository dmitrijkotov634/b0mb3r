from db0mb3r.services.service import Service


class DeliMobil(Service):
    async def run(self):
        await self.post(
            "https://api.delitime.ru/api/v2/signup",
            data={
                "SignupForm[username]": self.formatted_phone,
                "SignupForm[device_type]": 3,
            },
        )
