from dataclasses import dataclass
from datetime import datetime
@dataclass
class PushMessage: 
    title : str 
    id : str 
    time_stamp : datetime 
    mtype : str 