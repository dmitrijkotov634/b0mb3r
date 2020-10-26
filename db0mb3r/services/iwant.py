from db0mb3r.services.service import Service


class IWant(Service):
    async def run(self):
        await self.post(
            "https://i-want.ru/api/auth/v1/customer/login/phone",
            json={"phone": self.formatted_phone},
        )
