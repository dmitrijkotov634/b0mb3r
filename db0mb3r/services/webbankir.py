from db0mb3r.services.service import Service


class WebBankir(Service):
    async def run(self):
        await self.post(
            "https://ng-api.webbankir.com/user/v2/create",
            json={
                "lastName": self.russian_name,
                "firstName": self.russian_name,
                "middleName": self.russian_name,
                "mobilePhone": self.formatted_phone,
                "email": self.email,
                "smsCode": "",
            },
        )
