from db0mb3r.services.service import Service


class LogisticTech(Service):
    async def run(self):
        await self.post(
            "https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
            json={"phone": self.formatted_phone},
            headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"},
        )
