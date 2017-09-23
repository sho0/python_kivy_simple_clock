from kivy.app import App
from time import strftime
from kivy.clock import Clock
from kivy.uix.widget import Widget
import datetime

class Widgets(Widget):
    pass
class TestApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = strftime('%H:%M:%S')
        self.root.ids.date.text = strftime(datetime.date.today().strftime("%A") + ' %Y-%m-%d')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def build(self):
        return Widgets()
if __name__ == '__main__':
	TestApp().run()
