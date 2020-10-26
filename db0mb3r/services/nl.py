from db0mb3r.services.service import Service


class NovayaLinya(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://www.nl.ua",
            data={
                "component": "bxmaker.authuserphone.login",
                "sessid": "bf70db951f54b837748f69b75a61deb4",
                "method": "sendCode",
                "phone": self.formatted_phone,
                "registration": "N",
            },
        )
