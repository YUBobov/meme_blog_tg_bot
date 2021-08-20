import config
import requests

#api.vk.com/method/wall.get?access_token=d99a1dfed99a1dfed99a1dfed3d9e31e3edd99ad99a1dfeb884bcc9c1d6f3c1e2787b11&v=5.131&domain=thememeblog

def mempost():
    response = requests.get('http://api.vk.com/method/wall.get',
                            params = {
                                'access_token' : config.toeken_vk,
                                'v' : config.version_vk,
                                'domain' : config.domain,
                                'count': 1,

                            }
                            )
    data = response.json()['response']['items']
    #print(data)
    # s = 'https://vk.com/video-{0}_{1}'.format(data[1]['attachments'][0]['video']['owner_id'], data[1]['attachments'][0]['video']['id'])
    #
    return data
mempost()

#https://vk.com/video-120075923_456245205


