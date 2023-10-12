import asyncio
import logging
def periodic_asyinco(period):
    def schedule (func ) : 
         logging.log(logging.DEBUG ,"periodic task!!!")
         async def function(*args , **kwargs):
             while True : 
                 asyncio.create_task(func(*args, **kwargs)) 
                 await asyncio.sleep(period) 
         return function
    return schedule
