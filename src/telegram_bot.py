import telegram
import asyncio
import dotenv
import datetime 
from src.push import PushMessage
from zoneinfo import ZoneInfo
class TelegramNotificationBot(): 
    GROUP_ID = "-1001663929535"
    def __init__(self  , token ): 
        self.bot = telegram.Bot(token)
        self.event_loop =  asyncio.get_event_loop()
    
    def parse(message:PushMessage):
        return f"""
                  {message.mtype} : נשלח מ 
                """ +"\n" + message.title + f"""\n
                 בתאריך : {message.time_stamp.strftime('%d/%m/%Y, %H:%M')}
                """
    
    def handler(self , event  : PushMessage ):
        async def send_task():  
            await self.bot.send_message(text=TelegramNotificationBot.parse(event)  , chat_id = TelegramNotificationBot.GROUP_ID )
        time_diff = ( datetime.datetime.now().astimezone(ZoneInfo("Israel")) - event.time_stamp )
        if time_diff.total_seconds() <= ( 60 * 30  ) : # messages from the last 30 minutes 
            self.event_loop.create_task(send_task())  
        
    async def start(self): 
        await self.bot.initialize()

                
            
            
    