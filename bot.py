import telebot,time,request
from selenium import webdriver
from flask import Flask

#Add Your Telegram Bot Token Here
bot_token ="Your Bot Token Here"
bot = telebot.TeleBot(token=bot_token)

#Online Web browser/chrome driver (deployed on heroku)
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))

server = Flask(__name__)

#Local Web browser part
'''
chrome_options = webdriver.ChromeOptions()
CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
CHROMEDRIVER_PATH = 'C:\\APPDATA\\Python\\chromedriver.exe'
WINDOW_SIZE = "1920,1080"
chrome_options.add_argument("--headless") # comment out this line if you don't want to open browser in headless mode
chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
'''

#default Bot commands
@bot.message_handler(commands=['start']) 
def send_welcome(message):
    bot.reply_to(message,"Welcome To Magnet Link Scarpper Bot \n Send Any Movie Name You Will Get it's Magnet Link!")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Send Movie With Year That it was released To get better result...')

#this is main message handler it will receive input from any user if it's not empty it will run the at_answer function
@bot.message_handler(func = lambda msg: msg.text!="")
def at_answer(message):
    url="https://www.1337x.to/search/"+message.text+"/1/"
    driver.get(url)
    driver.get(url) 
    time.sleep(3)   
    try:
        for i in range(1,4): # change 4 to any number if you want more results than 3
            path = "//table/tbody/tr["+str(i)+"]/td[1]"
            driver.find_element_by_xpath(path).click()
            time.sleep(3)
            gg =driver.find_element_by_xpath("//div/div[2]/div[1]/ul[1]")
            href = gg.find_element_by_tag_name('a').get_attribute("href")
            name= driver.find_element_by_tag_name('h1') 
            nameofthetorrent = name.text[0:len(name.text)-2]  
            driver.get(url)
            i+=1
            bot.send_message(message.chat.id,text = "*_`{}`_* \n\n__`{}`__ ".format(nameofthetorrent,href),parse_mode='MarkdownV2') #Sends the top 3 magnet link with name of the torrent
    except:
        bot.send_message(message.chat.id,"No Torrent Available")

      
#webhooks (comment out this code if you want to run this this bot on your local machine)
@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200   
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://[Heroku Website NAME HERE].herokuapp.com/' + bot_token) # get your heroku app website from heroku.com
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
       
'''
#bot Polling (remove comments from this part if you want to run this code on your local machine
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
'''
