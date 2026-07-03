from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from board import Board


class LifeApp(App):

    def build(self):

        root = BoxLayout(orientation="vertical")

        self.board = Board()

        # Панель кнопок
        panel = BoxLayout(size_hint=(1, 0.1))

        btn_start = Button(text="▶ Start")
        btn_pause = Button(text="⏸ Pause")
        btn_clear = Button(text="🧹 Clear")
        btn_random = Button(text="🎲 Random")

        panel.add_widget(btn_start)
        panel.add_widget(btn_pause)
        panel.add_widget(btn_clear)
        panel.add_widget(btn_random)

        # связываем кнопки с действиями
        btn_start.bind(on_press=lambda x: self.board.start())
        btn_pause.bind(on_press=lambda x: self.board.stop())
        btn_clear.bind(on_press=lambda x: self.board.clear())
        btn_random.bind(on_press=lambda x: self.board.random_fill())

        root.add_widget(self.board)
        root.add_widget(panel)

        return root


if __name__ == "__main__":
    LifeApp().run()