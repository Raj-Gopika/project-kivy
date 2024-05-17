from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from timer import main_timer, break_timer

TIMER = 1500
BREAK_TIMER = 300

class BoxLayoutExample(BoxLayout):
    main_timer(TIMER)
    break_timer(BREAK_TIMER)
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
