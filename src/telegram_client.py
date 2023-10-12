from telethon import TelegramClient, events , utils 
import dotenv
import os 
import asyncio
import datetime
from zoneinfo import ZoneInfo
import src.push as push 
import src.observerable as observerable
class TelegramNotification(observerable.ObserverAble):
    client = None  
    @staticmethod
    async def singelton_factory(session_token , api_token , hash_token): 
        if not TelegramNotification.client : 
            TelegramNotification.client = TelegramClient(session_token , api_token , hash_token  )

            await TelegramNotification.client.start()
        return TelegramNotification.client
    
    def __init__(self , group_name  ): 
        observerable.ObserverAble.__init__(self) 
        self.group_name = group_name
        TelegramNotification.client.add_event_handler(self.trigger_event ,event=events.NewMessage(chats=group_name))
        print("cool1")
        
    async def start(): 
        await TelegramNotification.client.run_until_disconnected()
          
    async def parse(data): 
        sender = await data.get_sender()
        name = utils.get_display_name(sender)
        return push.PushMessage(title = data.message.message , mtype = "Telegram@" + name , time_stamp=data.message.date.astimezone(ZoneInfo("Israel"))  , id = ""  ) 
    
    async def trigger_event(self , event):
        if event.message.message : 
         self.call_observers(await TelegramNotification.parse(event))
        
def handler(message):
    print(message)
if __name__ == "__main__":
    TelegramNotification.singelton_factory()
    print('hello world ')
    tclient1 = TelegramNotification("IdanMaman")
    tclient2 = TelegramNotification("amitsegal")
    tclient3 = TelegramNotification("ynetalerts")
    tclient4 = TelegramNotification("Yediotnews")
    tclient1.add_observer(handler)
    tclient2.add_observer(handler)
    tclient3.add_observer(handler)
    tclient4.add_observer(handler)
    TelegramNotification.start()
    while True: 
        ...