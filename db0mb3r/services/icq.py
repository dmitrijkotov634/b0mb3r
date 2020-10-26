from db0mb3r.services.service import Service


class ICQ(Service):
    async def run(self):
        await self.post(
            "https://www.icq.com/smsreg/requestPhoneValidation.php",
            data={
                "msisdn": self.formatted_phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763",
            },
        )
