# shell_il_live
# stay updated in *live* on the war when you are in the shell or on our website (and in the future telegram bot) 

# How to use : 
create telegram client tokens and put them in `src/.env` file 

you can create them here : ```https://my.telegram.org``` `=> Api development tools` 
## Terminal version : 
```curl <ip> ```
## Website version 
just enter regularly to the website ... 


![Screenshot 2023-10-09 at 20 09 14](https://github.com/idanmaman2/shell_il_live/assets/90776557/81d0b154-866c-4e38-85e3-d4072326a6bc)
<img width="1468" alt="Screenshot 2023-10-10 at 21 00 51" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/0e3ff3f7-c86a-48ea-b3cb-9f91d6f97224">
![Screenshot 2023-10-10 at 21 01 23](https://github.com/idanmaman2/shell_il_live/assets/90776557/ca37f9ba-b540-433f-8aca-e11bac8c818e)
<img width="516" alt="Screenshot 2023-10-11 at 0 52 04" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/f414156a-bb5b-4ae2-bcd6-7639732932e5">
![image](https://github.com/idanmaman2/shell_il_live/assets/90776557/165b2975-cd11-4f04-aee5-66b86f73c329)

## the way that chrome's version works is a bit diffent because it doesnt support `multipart/x-mixed-replace`

<img width="1466" alt="Screenshot 2023-10-10 at 21 01 01" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/faf1f0fe-9b7b-4364-a3a5-1a44d1729c8a">

# SO HOW IT WORKS ? 

I used chunked http request  

Safari and FireFox support in multipart/x-mixed-replace which cleans the previous chunk 

but Curl and Chrome do not so with Curl I used Ansi codes to clean the screen and show the content in color 

In chrome I kept track on the id of each request and make the previous one vanish with css

Because keep alive max time I added http-equiv

and that is it kids - simple tricks to make live updated website with no effort or complex stuff 




