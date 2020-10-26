from db0mb3r.services.service import Service


class Pomodoro(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://butovo.pizzapomodoro.ru/ajax/user/auth.php",
            data={
                "AUTH_ACTION": "SEND_USER_CODE",
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
