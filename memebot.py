import config
import mempars
import telebot
import time

new_date= 0
file = open('date.txt', 'r')
last_date = file.read()
file.close()
print(last_date)
BOT_TOKEN = config.token_tg
channel = config.channel
bot = telebot.TeleBot(BOT_TOKEN)
#bot.config['api_key'] = BOT_TOKEN
#print(message.chat.type())

mem_post = mempars.mempost()
while True:
    for post in mem_post:
        if post['date'] > new_date:
        #if post['date'] > int(last_date) :

            if post['attachments'][0]['type'] == 'video':
                s = 'https://vk.com/video{0}_{1}?list={2}'.format(post['attachments'][0]['video']['owner_id'],
                                                          post['attachments'][0]['video']['id'],
                                                          post['attachments'][0]['video']['access_key'])
                bot.send_message(channel, '{0}\n\n{1}'.format(post['text'], s))
                #bot.send_video(channel, s, caption=post['text'])
                #bot.send_message(channel, post['text'])
                #bot.send_message(channel, s)
                #print('ssssdasdas\n\n\n')
                #print(s)
            elif post['attachments'][0]['type'] == 'photo':
                img = post['attachments'][0]['photo']['sizes'][-1]['url']
                bot.send_photo(channel, img, caption=post['text'])
            else:
                bot.send_message(channel, post['text'])
            file = open('date.txt', 'w')
            new_date = post['date']
            last_date = post['date']
            file.write(str(last_date))
            file.close()
    print('wait')
    time.sleep(int(60))
    print('agean')
bot.polling(non_stop = True)
