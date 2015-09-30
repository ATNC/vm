from django.shortcuts import render
import vk
from django.views.generic import TemplateView
import json
import requests
import urllib
import vkontakte
from django.contrib.auth.models import User
from slugify import slugify
import pwd

class GetInfo(TemplateView):
    template_name = 'index.html'



    def get_context_data(self, *args, **kwargs):
        key = pwd.APP_KEY


        login = pwd.LOGIN
        password = pwd.PASSWORD
        # u = User.objects.get(username=self.request.user).social_auth.first()
        # a_t = u.access_token
        # uid = u.uid
        # vkapi = vk.API(key, login, password, access_token=a_t)
        # audio = vkapi.audio.get(uid=uid, count='2')['items']
        # for items in audio:
        #
        # print len(audio)
        # req   = requests.get(audio[0].get('url'), stream=True)
        # title = audio[0].get('title')
        # # urllib.urlretrieve(audio[0].get('url'), 'test.mp3')
        # with open('music/%s.mp3'%title, 'wb') as music:
        #     music.write(req.content)
        #
        # print title



        context = super(GetInfo, self).get_context_data(*args, **kwargs)
        return context
# Create your views here.
