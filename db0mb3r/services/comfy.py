from db0mb3r.services.service import Service

class Comfy(Service):

    async def run(self):
        await self.post(
            "https://comfy.ua/ua/customer/account/createPost",
            data={"registration_name": self.russian_name, "registration_phone": self.formatted_phone, "registration_email": self.email}
        )

