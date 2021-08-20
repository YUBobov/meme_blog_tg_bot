import config
import mempars
import telebot
import time

new_date= 0
BOT_TOKEN = config.token_tg
channel = config.channel
bot = telebot.TeleBot(BOT_TOKEN)

while True:
    med_arr = []
    mem_post = mempars.mempost()
    for post in mem_post:
        if post['date'] > new_date:
            if len(post['attachments']) > 2:
                for i in range(len(post['attachments'])):
                    if post['attachments'][i]['type'] == 'video':
                        s = 'https://vk.com/video{0}_{1}?list={2}'.format(post['attachments'][i]['video']['owner_id'],
                                                                          post['attachments'][i]['video']['id'],
                                                                          post['attachments'][i]['video']['access_key'])
                        if not med_arr:
                            med_arr.append(telebot.types.InputMediaVideo(s, caption=post['text'][:1000]))
                        else:
                            med_arr.append(telebot.types.InputMediaVideo(s))

                    elif post['attachments'][i]['type'] == 'photo':
                        img = post['attachments'][i]['photo']['sizes'][-1]['url']
                        if not med_arr:
                            med_arr.append(telebot.types.InputMediaPhoto(img, caption=post['text'][:1000]))
                        else:
                            med_arr.append(telebot.types.InputMediaPhoto(img))

                bot.send_media_group(channel, med_arr)
            else:
                if post['attachments'][0]['type'] == 'video':
                    s = 'https://vk.com/video{0}_{1}?list={2}'.format(post['attachments'][0]['video']['owner_id'],
                                                              post['attachments'][0]['video']['id'],
                                                              post['attachments'][0]['video']['access_key'])
                    bot.send_message(channel, '{0}\n\n{1}'.format(post['text'], s))
                elif post['attachments'][0]['type'] == 'photo':
                    img = post['attachments'][0]['photo']['sizes'][-1]['url']
                    bot.send_photo(channel, img, caption=post['text'])
                else:
                    bot.send_message(channel, post['text'])
            new_date = post['date']

    print('wait')
    time.sleep(int(60))
    print('agean')
#bot.polling(non_stop = True)
