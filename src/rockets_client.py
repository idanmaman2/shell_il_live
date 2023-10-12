import src.observerable as observerable
import src.push as push  
import httpx
from http.cookiejar import parse_ns_headers
import src.periodic_loop as periodic_loop
import hashlib 
import datetime 
from zoneinfo import ZoneInfo
from src.config import MAX_IDS_PERIODIC
class RocketsClient(observerable.ObserverAble):
    __url  = """https://www.oref.org.il//WarningMessages/History/AlertsHistory.json""" 
    cookies_string = """Lastalerts=; AlertSoundNewFeature=1; _hjFirstSeen=1; _hjIncludedInSessionSample_2052890=0; _hjSession_2052890=eyJpZCI6IjZiMzA2MGM1LTMyNGMtNDBhYy1iODUyLWU3YTM0MWMyZTI3OCIsImNyZWF0ZWQiOjE2OTY4NDQ5Nzc1MTcsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; _gid=GA1.3.775484742.1696844978; _gat_UA-161451162-1=1; UsId=E547XSXP-BR6X-8P8J-BMFU-GCKE3BQU94B6; _fbp=fb.2.1696844977941.380775209; _ga_V2BQHCDHZP=GS1.1.1696844977.1.1.1696845001.36.0.0; _ga=GA1.1.1413759987.1696844978; _hjSessionUser_2052890=eyJpZCI6ImUxMGNiYzY0LTkxOTEtNWY0Ny1hMmY2LWNmNjIwYzM1MTEwZiIsImNyZWF0ZWQiOjE2OTY4NDQ5Nzc1MTYsImV4aXN0aW5nIjp0cnVlfQ==; mp_cff7389ad1aba4a6b7f9631edf8f6234_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18b13d795fe3b2-09a85888fbd2c1-6034535a-157188-18b13d795fe3b2%22%2C%22%24device_id%22%3A%20%2218b13d795fe3b2-09a85888fbd2c1-6034535a-157188-18b13d795fe3b2%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22__alias%22%3A%20%22E547XSXP-BR6X-8P8J-BMFU-GCKE3BQU94B6%22%2C%22%24user_id%22%3A%20%22E547XSXP-BR6X-8P8J-BMFU-GCKE3BQU94B6%22%7D"""
    cookies = dict(map(lambda x : x[0] , parse_ns_headers(cookies_string.split(";"))))
    userAgent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36"""
    def __init__(self): 
        observerable.ObserverAble.__init__(self)
        self.client = httpx.AsyncClient()
        self.cached_ids = [] 
        
    @periodic_loop.periodic_asyinco(30)
    async def start(self): 
        try : 
            respone = await self.client.get(RocketsClient.__url ,cookies= RocketsClient.cookies ,   headers={ "User-Agent" :RocketsClient.userAgent}) 
            self.trigger(respone.json())
        except :
            ...
    
    def trigger(self ,messages ) : 
        for message in reversed(messages) : 
             pmessage = RocketsClient.parse(message)
             if pmessage.id not in self.cached_ids : 
                 print("Rocket Alert")
                 self.cached_ids.append(pmessage.id)
                 self.call_observers(pmessage)
                 self.cached_ids = self.cached_ids[-MAX_IDS_PERIODIC:]
                 
    def parse(data): 
        return push.PushMessage(title=data["data"] + " " + "צבע אדום" ,time_stamp= datetime.datetime.strptime(data["alertDate"] , "%Y-%m-%d %H:%M:%S" ).astimezone(ZoneInfo("Israel")) ,  id= hashlib.md5((data["title"]+data["alertDate"]).encode()).hexdigest() , mtype="ROCKETS" ) 

