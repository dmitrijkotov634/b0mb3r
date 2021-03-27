from db0mb3r.services.service import Service

class CashU(Service):
    phone_codes = [7]
    
    async def run(self):
        await self.post(
            "https://cash-u.com/main/rest/firstrequest/phone/confirmation/send",
            data=(self.format(self.formatted_phone, '* (***) ***-**-**:'))
        )