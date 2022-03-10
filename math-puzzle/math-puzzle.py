from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import webbrowser
import random

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from arithmetric import Arithmetic


################################################################################

class MathPuzzleRoot(BoxLayout):
    """Root of all widgets
    """
    math_screen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(MathPuzzleRoot, self).__init__(**kwargs) 
         # List of previous screens
        self.screen_list = []
        self.is_mix = False

    def changeScreen(self, next_screen):
        operations = "addition subtraction multiplication division".split()
        question = None

        # If screen is not already in the list fo prevous screens
        if self.ids.kivy_screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.kivy_screen_manager.current)

        if next_screen == "about this game":
            self.ids.kivy_screen_manager.current = "about_screen"

        else:
            if next_screen == "mix!":
                self.is_mix = True
                index = random.randint(0, len(operations) - 1)
                next_screen = operations[index]
            else:
                self.is_mix = False
            for operation in operations:
                if next_screen == operation:
                    question = f"self.math_screen.get_{operation}_question()"
            self.math_screen.question_text.text = MathPuzzleRoot.prepQuestion(
                eval(question) if question is not None else None
            )
            self.ids.kivy_screen_manager.current = "math_screen"

    @staticmethod
    def prepQuestion(question):
        " Prepares a math question with markup "
        if question is None:
            return "ERROR"
        text_list = question.split()
        text_list.insert(2, "[b]")
        text_list.insert(len(text_list), "[/b]")
        return " ".join(text_list)
    

    def onBackBtn(self):
        # Check if there are any screen to go back to
        if self.screen_list:
            # if there are screens we can go back to, the just do it
            self.ids.kivy_screen_manager.current = self.screen_list.pop()
            # Saw we don't want to close
            return True
        # No more screens to go back to
        return False

###############################################################################

class MathScreen(Screen, Arithmetic):
    """Widget that will arc as a screen and hold funcs for math questions
    
    """  
    def __init__(self, *args, **kwargs):
        super(MathScreen, self).__init__(*args, **kwargs)

###############################################################################

class KivyTutorApp(App):
    """App object

    """
    def __init__(self, **kwargs):
        super(KivyTutorApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        # user presses back button
        if key == 27:
            return self.root.onBackBtn()


    def build(self):
        return MathPuzzleRoot()

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