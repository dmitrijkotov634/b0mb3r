from db0mb3r.services.service import Service


class Pliskov(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": self.format(self.formatted_phone, "+* (***) ***-**-**")},
        )
