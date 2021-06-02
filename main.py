from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView

import requests
import json

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


Window.size = (480, 853)


from kivymd.app import MDApp


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class LocationMap(MapView):
    pass


def check_number(number):
    with open('data.json', 'r') as file:
        data = file.read()
        if data == '':
            return True
        else:
            data = json.loads(data)
            if str(data['number']) == str(number):
                return True
            else:
                return False


def get_data(number):
    if len(number) != 11 or number == '':
        return {
            "ip": 'ERROR',
            "city": 'INCORRECT',
            "region": 'NUMBER',
            "country": 'PLEASE',
            "loc": 'TRY',
            "org": 'ANOTHER',
            "timezone": 'NUMBER',
            "readme": 'NUMBER'
        }

    if check_number(number):
        with open('data.json', 'w') as f:
            url = 'http://ipinfo.io'
            response = requests.get(url).json()
            response['number'] = number
            json.dump(response, f, ensure_ascii=False)
        return response
    else:
        return {
            "ip": 'EXIST',
            "city": 'PHONE',
            "region": 'NUMBER',
            "country": 'PLEASE',
            "loc": 'TRY',
            "org": 'ANOTHER',
            "timezone": 'PHONE',
            "readme": 'NUMBER'
        }


class Container(GridLayout):

    def calculate(self):
        try:
            number = self.text_input.text
        except:
            number = ''

        data = get_data(number)

        self.ip.text = data['ip']
        self.city.text = data['city']
        self.reg.text = data['region']
        self.country.text = data['country']
        self.loc.text = data['loc']
        self.host.text = data['org']
        self.tzone.text = data['timezone']


class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls.theme_style = "Dark"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
