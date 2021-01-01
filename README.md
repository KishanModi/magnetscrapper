# Torrent Magnet Link Scrapper Bot
## A telegram bot which Gives You the magnet link of any torrent you want to download From 1337x.to

<hr>

## Requirements
- Get [Python](https://python.org)
- Git

## Instructions

### Following method works same for linux,win,android(termux)

### Get the package
```
$ git clone https://github.com/kishanmodi/magnetscrapper
```

```
$ cd magnetscrapper
```

### Install required packages
```
$ pip install -r requirements.txt
```
- Get your bot token from [BotFather](https://telegram.me/BotFather)

### Set Bot token in Python
```
{
    bot_token="Your_bot_token_here"
}
```

## Follow this to run this bot on local machine

# Remove Comment from the following parts of the code
- #Local Web browser part
- #bot Polling 

#### Comment Out the following parts of the code
- #webhooks
- #Online Web browser/chrome driver

#### Once its finished start the script! and Relax!
```
$ python bot.py
```

## Follow this to run this bot on heroku server

- Install Heroku cli
- go to heroku.com and create a new account than create a new app
- add bellow mentioned config vars and bulidpacks

#### BulidPacks
```
heroku/python
https://github.com/heroku/heroku-buildpack-google-chrome
https://github.com/heroku/heroku-buildpack-chromedriver
```
#### Config Vars
```
key: CHROMEDRIVER_PATH, value: /app/.chromedriver/bin/chromedriver
key: GOOGLE_CHROME_BIN, value: /app/.apt/usr/bin/google-chrome
```
#### Add your heroku website in your code
```
bot.set_webhook(url='https://[Heroku Website NAME HERE].herokuapp.com/' + bot_token)
```
### Deploy The bot to heroku
```
$ git init
$ git add .
$ git commit -am "make it better"
$ git push heroku main
```

<hr>

## Issues
if you face any kind of issue then please let me know on [telegram](https://t.me/kishanmodi)

<hr>

## License
&copy; Kishan Modi (UnLicnesed/Free to use) 
