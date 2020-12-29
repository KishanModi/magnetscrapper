import telebot,time,os
from selenium import webdriver
from flask import Flask, request


options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))

'''
#web_browser modeule part
chrome_options = webdriver.ChromeOptions()
CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
CHROMEDRIVER_PATH = 'C:\\APPDATA\\Python\\chromedriver.exe'
#WINDOW_SIZE = "1920,1080"
#chrome_options.add_argument("--headless")
chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
'''

bot_token ="1214469450:AAGBb_JuNQ2EdKCrkbbfoHUDPExJMhVH_cU"
bot = telebot.TeleBot(token=bot_token)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Welcome To Magnet Link Scarpper Bot \n Send Any Movie Name You Will Get it's Magnet Link!")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Send Movie With Year That it was released To get better result...')

@bot.message_handler(commands=['stop'])
def send_stop(message):
    bot.reply_to(message,'Stopped')


@bot.message_handler(func = lambda msg: msg.text!="stop")
def at_answer(message):
    n=0
    url="https://www.1337x.to/search/"+message.text+"/1/"
    driver.get(url)
    driver.get(url)
    print(str(driver.current_url))   
    time.sleep(3)   
    try:
        for i in range(1,4):
            path = "//table/tbody/tr["+str(i)+"]/td[1]"
            print(path)
            driver.find_element_by_xpath(path).click()
            time.sleep(3)
            gg =driver.find_element_by_xpath("//div/div[2]/div[1]/ul[1]")
            href = gg.find_element_by_tag_name('a').get_attribute("href")
            print(href)
            name= driver.find_element_by_tag_name('h1')
            print(name.text)
            print(type(name.text))
            x = len(name.text)
            print(x)
            na = name.text[0:x-2]
            print(na)
            driver.get(url)
            i+=1
            bot.send_message(message.chat.id,text = "*_`{}`_* \n\n__`{}`__ ".format(na,href),parse_mode='MarkdownV2')
    except:
        bot.send_message(message.chat.id,"No Torrent Available")
    

@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200   

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://magnetscrapper.herokuapp.com/' + bot_token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
    
    
'''

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
'''