from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from pyowm import OWM
from pyowm.utils.config import get_default_config

dict_config = get_default_config()
dict_config['language'] = 'ru'
owm = OWM('b4b0d66c2ce98910ec76c34c32e26dee')
mgr = owm.weather_manager()


class mainApp(App):
    def build(self):
        bl = BoxLayout()
        btn = Button(text="Search", font_size="50", size_hint=(.6, 1))
        self.lb = Label(text='', font_size='28')
        self.ti = TextInput(font_size='50', size_hint=(.6, 1))
        btn.bind(on_release=self.weather)
        bl.add_widget(btn)
        bl.add_widget(self.lb)
        bl.add_widget(self.ti)
        return bl

    def weather(self, instanse):
        try:
            global mgr
            observation = mgr.weather_at_place(self.ti.text)
            w = observation.weather
            t = w.temperature('celsius')
            temp = t['temp']
            temp_max = t['temp_max']
            temp_min = t['temp_min']
            feels = t['feels_like']

            speed = w.wind()['speed']
            state = w.detailed_status
            clouds = w.clouds
            humidity = w.humidity

            self.lb.text = 'Температура в городе\стране-\n' + self.ti.text + ': ' + str(
                temp) + 'C°' + '\nМинимальная: ' + str(temp_min) + 'C°' + '\nМаксимальная: ' + str(
                temp_max) + 'C°' + '\nОщущается как: ' + str(feels) + 'C°' + '\nСкорость ветра: ' + str(
                speed) + 'мс' + '\nCостояние: ' + state + '\nОблака: ' + str(clouds) + '%' + '\nВлажность: ' + str(
                humidity) + '%'
        except:
            self.lb.text = "Такого города не найдено!"


if __name__ == '__main__':
    mainApp().run()