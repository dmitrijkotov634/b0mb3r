from db0mb3r.services.service import Service


class Avtoobzvon(Service):
    phone_codes = [7]

    async def run(self):
        await self.get(
            "https://avtobzvon.ru/request/makeTestCall",
            params={"to": self.format(self.phone, "(***) ***-**-**")},
        )
