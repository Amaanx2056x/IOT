import telepot

token = '1329377783:AAHNgLKw7FOGdNMG4zWsEXI6t0y2948TeJM'
bot = telepot.Bot(token)
print (bot.getMe())

##https://api.telegram.org/bot1329377783:AAHNgLKw7FOGdNMG4zWsEXI6t0y2948TeJM/getUpdates
##https://api.telegram.org/bot1329377783:AAHNgLKw7FOGdNMG4zWsEXI6t0y2948TeJM/sendMessage?chat_id=1347378905&text=Hii There

def handle(msg):
  content_type = telepot.glance(msg)
  chat_type=telepot.glance(msg)
  chat_id=telepot.glance(msg)
  print(content_type, chat_type, chat_id)

  if content_type == 'text':
    bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
    
bot.message_loop(handle)
