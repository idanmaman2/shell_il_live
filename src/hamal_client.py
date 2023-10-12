import socketio
import logging
import src.push as push 
import src.observerable as observerable
from termcolor import colored
import datetime 
from src.config import MAX_IDS
from zoneinfo import ZoneInfo
class HamalNotification(socketio.ClientNamespace , observerable.ObserverAble): 
    
    __url = """https://public-api.hamal.co.il/socket.io/"""
    
    def __init__(self) : 
        super(socketio.ClientNamespace , self ).__init__("/")
        observerable.ObserverAble.__init__(self)
        #setup socketio connection 
        sio = socketio.Client()
        sio.register_namespace(self)
        sio.connect(HamalNotification.__url , namespaces = ["/"] )
        logging.log(logging.DEBUG ,"init HAMAL")
        self.sio = sio 
        self.counter =0 
        self.cached_ids = [] 
        
    def on_connect(self):
        logging.log(logging.DEBUG ,"Connected to Hamal ")
    
    def on_disconnect(self):
        logging.log(logging.DEBUG ,"THERE IS A PROBLEM WITH HAMAL ")
        
    def parse(message):
        return push.PushMessage(time_stamp=datetime.datetime.fromtimestamp(message["publishedAt"] / 1000 ).astimezone(ZoneInfo("Israel")) ,  title =  message['metaData']['slugTitle'].replace('-',' ') +" :: " +message["metaData"]["description"]  , id = message["_id"] , mtype = "HAMAL" ) 
    
    def trigger_event(self, event_name , *args  ):
        if len(args) == 1 : 
            data = args[0]
            if  data["_id"] not in self.cached_ids : 
                self.cached_ids.append(data["_id"])
                self.call_observers(HamalNotification.parse(data))
                self.cached_ids = self.cached_ids[-MAX_IDS:]