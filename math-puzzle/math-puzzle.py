from kivy.app import App
from kivy.uix.label import Label


class MathScreen:
    pass

class MathPuzzleApp(App):
    def build(self):
        return Label(text="Hello,\n Welcome to MathPuzzle First Build!", font_size=50)


if __name__ == "__main__":
    app = MathPuzzleApp()
    app.run()
