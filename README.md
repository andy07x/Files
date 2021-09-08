## Simple Bot with queue work 
Only for single users [u can modify it for many users but queue wont work ]

## ffmpeg compiled with libfdk_aac 🎉

This repo can be deployed on heroku by connecting github to heroku and cloning or fork this repo 
This repo is compiled with libfdk_aac, and thanks to me and my friend  to do this 
If u want to compile libfdk_aac in ur repo just copy paste my dockerfile there 
[Note: This repo needs atleast 25 mins to build and 5 to 7 mins to deploy ]
## Deploy on Railway 
Railway.app 👈

1)I suggest u to clone Or Just Fork this repo

2)Then go to <a href="railway.app" target="_blank">Railways</a>

3)Then make fake cc (If Don't Know Ask ,<a href="https://telegram.dog/Kai_8_4">@Kai_8_4</a> and buy developer pack (as starter pack isnt copacetic for encoding)

4)Then click variable and add this

## Deploy With Heroku (It Will Take 25min)

<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-green?style=for-the-badge&logo=heroku" width="200""/></a></p>

### Variables
`APP_ID` : Get Your APP_ID From my.telegram.org or [@TeleORG_Bot](https://telegram.dog/TeleORG_Bot).

`API_HASH` : Get Your APP_HASH From my.telegram.org or [@TeleORG_Bot](https://telegram.dog/TeleORG_Bot).

`BOT_TOKEN` : Your Telegram Bot Token From [@BotFather](https://telegram.dog/Botfather).

`OWNER` : Put ID Of Auth Users with a space between it. 

*Note: Don't Use More Than 2 ID's Or Else Queue Function May Not Work*.

`THUMBNAIL` : Put telegraph link of a picture for use of Thumbnail using A Bot or Use `/bash wget <Telegraph Link> -O "thumb.jpg"`

`FFMPEG` : Put Your FFMPEG Code with "{}" as input and output. (Eg. `ffmpeg -i "{}" -preset veryfast -vcodec libx265 -crf 27 "{}"`)

## Credits

- [Kai84](https://telegram.dog/Kai_8_4) For Merging and Deployable To Heroku

- [Rick-and-Roll](https://telegram.dog/Just_REV3RSE) For Making `libfdk-aac` In Compress Queue

- [1Danish-00](https://github.com/1Danish-00) For Compressor Bot


<b>Source : </b>[Main Source](https://github.com/Dragonpower84/CompressorBot)
