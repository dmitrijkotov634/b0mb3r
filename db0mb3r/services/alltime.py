from db0mb3r.services.service import Service


class Alltime(Service):
    phone_codes = [7]

    async def run(self):
        await self.post("https://www.alltime.ru/sservice/2020/form_register_phone.php",
                        data={"action": "send", "back": "/",
                              "phone": self.format(self.formatted_phone, "+* (***) ***-**-**")})
