from db0mb3r.services.service import Service


class SmartSpace(Service):
    async def run(self):
        await self.post(
            "https://smart.space/api/users/request_confirmation_code/",
            json={"mobile": "+" + self.formatted_phone, "action": "confirm_mobile"},
        )
