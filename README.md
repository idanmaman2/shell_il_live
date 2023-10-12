<img width="1470" alt="Screenshot 2023-10-10 at 2 08 09" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/b25ba2dc-2176-4f5a-abee-f391f3fb8011"><img width="1465" alt="Screenshot 2023-10-10 at 2 08 13" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/b8237af0-c6c8-4f4b-bcc2-9a17d8fdda56"># shell_il_live
# stay updated in *live* on the war when you are in the shell or on our website (and in the future telegram bot) 

# How to use : 
create telegram client tokens and put them in `src/.env` file 

you can create them here : ```https://my.telegram.org``` `=> Api development tools` 
## Terminal version : 
```curl <ip> ```
## Website version 
just enter regularly to the website ... 
<img width="1465" alt="Screenshot 2023-10-10 at 2 08 13" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/7bf07bde-5b86-46a2-ac10-ec60d9935422">

<img width="1466" alt="Screenshot 2023-10-10 at 11 22 53" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/f6b753f4-5bf9-4bb6-abe2-e6fed9b080bd">

![Screenshot 2023-10-09 at 19 39 12](https://github.com/idanmaman2/shell_il_live/assets/90776557/e2a5f056-ec4d-4b61-932b-b0adb23991df)

<img width="585" alt="Screenshot 2023-10-10 at 23 53 33" src="https://github.com/idanmaman2/shell_il_live/assets/90776557/a162f263-1395-4162-8d4e-58d449ed5fc9">


## the way that chrome's version works is a bit diffent because it doesnt support `multipart/x-mixed-replace`


# SO HOW IT WORKS ? 

I used chunked http request  

Safari and FireFox support in multipart/x-mixed-replace which cleans the previous chunk 

but Curl and Chrome do not so with Curl I used Ansi codes to clean the screen and show the content in color 

In chrome I kept track on the id of each request and make the previous one vanish with css

Because keep alive max time I added http-equiv

and that is it kids - simple tricks to make live updated website with no effort or complex stuff 




