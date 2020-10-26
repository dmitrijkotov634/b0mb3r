from db0mb3r.services.service import Service


class MenuUA(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            data={
                "user_info[fullname]": self.russian_name,
                "user_info[phone]": self.formatted_phone,
                "user_info[email]": self.email,
                "user_info[password]": self.password,
                "user_info[conf_password]": self.password,
            },
        )
        await self.post(
            "https://www.menu.ua/kiev/delivery/profile/show-verify.html",
            data={"phone": self.formatted_phone, "do": "phone"},
        )
