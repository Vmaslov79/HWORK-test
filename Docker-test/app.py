from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import NumericProperty
import random

class BallGame(Widget):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball = Label(text="⚽", font_size=50, pos=(200, 400))
        self.add_widget(self.ball)
        Clock.schedule_interval(self.move_ball, 1)

    def move_ball(self, dt):
        # Рухаємо м'яч у випадкове місце
        self.ball.pos = (random.randint(0, 300), random.randint(0, 600))

    def on_touch_down(self, touch):
        # Якщо тицьнув по м’ячу → +1 бал
        if self.ball.collide_point(*touch.pos):
            self.score += 1
            print(f"Score: {self.score}")

class BallApp(App):
    def build(self):
        return BallGame()

if __name__ == "__main__":
    BallApp().run()
