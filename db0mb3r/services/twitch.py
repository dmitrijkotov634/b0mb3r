from db0mb3r.services.service import Service


class Twitch(Service):
    async def run(self):
        await self.post(
            "https://passport.twitch.tv/register?trusted_request=true",
            json={
                "birthday": {"day": 11, "month": 11, "year": 1999},
                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "include_verification_code": True,
                "password": self.password,
                "phone_number": self.formatted_phone,
                "username": self.username,
            },
        )
