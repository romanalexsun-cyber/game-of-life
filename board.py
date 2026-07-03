from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from game import Game
from kivy.clock import Clock
import random


class Board(Widget):

    CELL_SIZE = 20

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 30
        self.rows = 30
        self.game = Game(self.rows, self.cols)

        self.bind(size=self.redraw)
        self.bind(pos=self.redraw)
        self.running = False
        self.event = None
        self.speed = 5  # шагов в секунду

    def redraw(self, *args):

        self.canvas.clear()

        with self.canvas:

            Color(1, 1, 1)

            Rectangle(
                pos=self.pos,
                size=self.size
            )

            Color(0.8, 0.8, 0.8)

            for x in range(self.cols + 1):
                Line(points=[
                    x * self.CELL_SIZE,
                    0,
                    x * self.CELL_SIZE,
                    self.rows * self.CELL_SIZE
                ])

            for y in range(self.rows + 1):
                Line(points=[
                    0,
                    y * self.CELL_SIZE,
                    self.cols * self.CELL_SIZE,
                    y * self.CELL_SIZE
                ])

            # <<< Всё ещё внутри with!

            Color(0.2, 0.7, 0.2)

            for row in range(self.rows):
                for col in range(self.cols):

                    if self.game.field[row][col]:
                        Rectangle(
                            pos=(
                                col * self.CELL_SIZE + 1,
                                row * self.CELL_SIZE + 1
                            ),
                            size=(
                                self.CELL_SIZE - 2,
                                self.CELL_SIZE - 2
                            )
                        )

    def update(self, dt):
        print("TICK")
        self.game.step()
        self.redraw()

    def on_touch_down(self, touch):
        print("Нажали!", touch.x, touch.y)
        col = int(touch.x // self.CELL_SIZE)
        row = int(touch.y // self.CELL_SIZE)

        if 0 <= row < self.rows and 0 <= col < self.cols:
            if touch.button == "left":
                self.game.field[row][col] = not self.game.field[row][col]
            elif touch.button == "right":
                self.toggle()

            self.redraw()
        return True

    def toggle(self):
        if self.running:
            self.running = False
            Clock.unschedule(self.update)
        else:
            self.running = True
            Clock.schedule_interval(self.update, 1 / 5)

    def start(self):
        if not self.running:
            self.running = True
            self.event = Clock.schedule_interval(self.update, 1 / self.speed)

    def stop(self):
        if self.running:
            self.running = False
            if self.event:
                self.event.cancel()
                self.event = None

    def clear(self):
        self.game.field = [
            [False for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
        self.redraw()

    def random_fill(self):

        for row in range(self.rows):
            for col in range(self.cols):
                self.game.field[row][col] = random.random() < 0.2

        self.redraw()