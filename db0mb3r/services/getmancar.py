from db0mb3r.services.service import Service


class Getmancar(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://crm.getmancar.com.ua/api/veryfyaccount",
            json={
                "phone": "+" + self.formatted_phone,
                "grant_type": "password",
                "client_id": "gcarAppMob",
                "client_secret": "SomeRandomCharsAndNumbersMobile",
            },
        )
