from db0mb3r.services.service import Service

class SaveTime(Service):
    async def run(self):
        await self.post(
            "https://api.savetime.net/v2/client/login/" + self.formatted_phone,
            data='$------WebKitFormBoundaryVn8pvqIINnHzFQS4\\r\\nContent-Disposition: form-data; name="accept"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundaryVn8pvqIINnHzFQS4--\\r\\n',
            headers={
                "Connection": "keep-alive",
                "X-HASH": "c625e41dcf708c70aec75d9219846249",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207",
                "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryVn8pvqIINnHzFQS4",
                "Origin": "https://savetime.net",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://savetime.net/?sidebar_open=login",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            },
        )
