"""FastAPI server that sends chunked data to curl and shows it as is """
from fastapi import FastAPI, Header, Request
from fastapi.responses import StreamingResponse
import asyncio
import logging 
import bisect
import sys
import src.hamal_client as hamal_client
from termcolor import colored
import time 
from src.config import MAX_PUSHES,MAX_BROWSER,MAX_CURL
from typing import Annotated,Union
from src.rockets_client import RocketsClient
from src.telegram_client import TelegramNotification
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.telegram_bot import TelegramNotificationBot
import dotenv 
import os 
app = FastAPI() 
app.mount("/static", StaticFiles(directory="static"), name="static")
templates =  Jinja2Templates(directory="templates")
pushes = [] 
last_update = time.time()
bannerCurl = "\t\t" + colored(("SHELL_IL 🇮🇱") , "white" ,"on_blue", attrs=[])  + colored((" LIVE🔴") , "blue" ,"on_white", attrs=['blink'])  + "\n"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def handler(message): 
    global last_update
    global pushes
    print( message )
    bisect.insort_right(pushes,message , key= lambda x : x.time_stamp)
    pushes = pushes[-MAX_PUSHES:]
    last_update = time.time() 
    

def MessageParseCurl(message): 
    return colored(f"""{message.mtype}""", "white" , "on_light_red" , attrs=["bold" ]) + "\n" +  colored(f"""{message.title}"""  , "light_red" , "on_white") + "\n" + colored(f"""{message.time_stamp.strftime('%d/%m/%Y, %H:%M')}""" , "red" , "on_white", attrs=['underline'])
@app.get('/ping')
def ping(request: Request):
    return templates.TemplateResponse("pong.html",{"request": request})
@app.get('/')
async def streamALL(request: Request, user_agent: Annotated[Union[str, None], Header()] = None) : 
    async def iterfile():
        idcnt=0
        client_last_update = 0 
        while True :
            if user_agent : 
                if client_last_update < last_update :  
                    client_last_update = last_update 
                    if "curl" in user_agent : 
                        body =  "\n".join(map(lambda x : MessageParseCurl(x)   , reversed(pushes[-MAX_CURL:])))
                        yield ('--frame\r\n' 'Content-Type: text/plain; charset=utf-8\r\n\r\n' +'\x1b[2J\x1b[H' + 
                        bannerCurl +body +"\n " + '\r\n')
                        wtime = 10 
                    elif "Chrome" in user_agent : 
                        wtime = 0.1
                        idcnt+=1  
                        print(idcnt)
                        template =  templates.get_template("chrome_push.html")
                        body = template.render({"messages" : reversed(pushes[-MAX_BROWSER:])  , "id" : idcnt })
                        yield body
                    else : 
                        wtime = 0.1
                        template =  templates.get_template("push.html")
                        body = template.render({"messages" : reversed(pushes[-MAX_BROWSER:]) })
                        yield ('--frame\r\n' 'Content-Type: text/html; charset=utf-8\r\n\r\n'  + 
                         body + '\r\n')
            await asyncio.sleep(wtime)
    if "Chrome" in user_agent :
        media_type = "text/html"
    else : 
        media_type = "multipart/x-mixed-replace;boundary=frame"
    return StreamingResponse(iterfile(), media_type=media_type , headers={'X-Content-Type-Options': 'nosniff' , "Transfer-Encoding": "chunked" , "Cache-Control": "no-cache" , "Connection": "keep-alive" })



async def set_up(): 
    await TelegramNotification.singelton_factory(os.getenv('TG_SESSION'),os.getenv('TG_API_ID') , os.getenv('TG_API_HASH'))

    tclient2 = TelegramNotification("amitsegal")
    tclient3 = TelegramNotification("ynetalerts")
    tclient4 = TelegramNotification("Yediotnews")
    tclient5 = TelegramNotification("abualiexpress") 
    tclient6 = TelegramNotification("divuchimbizmanemet") 
    telegramBot = TelegramNotificationBot(os.environ["BOT_TOKEN"])
    hclient = hamal_client.HamalNotification()
    hclient.add_observer(handler,telegramBot.handler)
    rclient =  RocketsClient()
    rclient.add_observer(handler,telegramBot.handler)
    tclient1 = TelegramNotification("IdanMaman")
    tclient1.add_observer(handler , telegramBot.handler) 
    tclient2.add_observer(handler , telegramBot.handler)
    tclient3.add_observer(handler , telegramBot.handler) 
    tclient4.add_observer(handler , telegramBot.handler) 
    tclient5.add_observer(handler , telegramBot.handler)
    tclient6.add_observer(handler , telegramBot.handler)
    await asyncio.gather(telegramBot.start(),rclient.start() , TelegramNotification.start())


@app.on_event("startup")
async def main() :  
    dotenv.load_dotenv()
    asyncio.create_task(set_up()) 
    
if __name__ == "__main__":
  import uvicorn
  uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)     
     
     
