from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import webbrowser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


################################################################################

class KivyTutorRoot(BoxLayout):
    """Root of all widgets
    """
    def __init__(self, **kwargs):
        super(KivyTutorRoot, self).__init__(**kwargs)

    def changeScreen(self, next_screen):
        operations = "addition subtraction multiplication division".split()
        question = None

        if next_screen == "about this game":
            self.ids.kivy_screen_manager.current = "about_screen"


################################################################################

class KivyTutorApp(App):
    """App object

    """
    def __init__(self, **kwargs):
        super(KivyTutorApp, self).__init__(**kwargs)

    def build(self):
        return KivyTutorRoot()

    def getText(self):
        return ("Hello world!\n"
                "This is Math-puzzle project of 03-01\n"
                "\nKamolchanok  Chuchuen      6410110005\n"
                "Thanaphat   Pethdongjan    6410110207\n"
                "Thanawan   Saechiang       6410110210\n"
                "Nureeyah   Hayichesoh      6410110280\n"
                "Burhanurdin  Sa-ong        6410110289\n"
                "Chatchai   Jankaew         6410110644\n"
                "\nTo look at Math-puzzle source code on GitLab click "
                "[b][ref=source]\nMATH_PUZZLE\n[/ref][/b]\n")

    def on_ref_press(self, instance, ref):
        _dict = {
            "source": "https://gitlab.psu.ac.th/6410110207/math-puzzle",
        }

        webbrowser.open(_dict[ref])


if __name__ == '__main__':
    KivyTutorApp().run()