from db0mb3r.services.service import Service


class Sushi33(Service):
    phone_codes = [380]

    async def run(self):
        await self.get(
            "https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": self.email,
                "password": self.password,
                "phone": self.phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
