from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import webbrowser
import random

from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex

from arithmetric import Arithmetic

# Color the background
Window.clearcolor = get_color_from_hex("#79addc")

# Register fonts
LabelBase.register(
    name="Roboto",
    fn_regular="./fonts/Roboto-Thin.ttf",
    fn_bold="./fonts/Roboto-Medium.ttf"
)

################################################################################

class MathPuzzleRoot(BoxLayout):
    """
    Root of all widgets
    """
    math_screen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(MathPuzzleRoot, self).__init__(**kwargs) 
         # List of previous screens
        self.screen_list = []
        self.is_mix = False
        self.math_popup = MathPopup()

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
class MathPopup(Popup):
    GOOD = "{} :D"
    BAD = "{}, Correct answer is [b]{}[/b]"
    GOOD_LIST = ["Awesome!", "Amazing!", "Excellent!", "Correct!", "Genius!", "Pang mai wai!"]
    BAD_LIST = ["Almost!", "Close!", "Sorry", "Don't Worry", "On Doi Arr~"]

    message = ObjectProperty()
    wrapped_button = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(MathPopup, self).__init__(*args, **kwargs)
    
    def open(self, correct=True):
        if correct:
            if self.wrapped_button in self.content.children:
                self.content.remove_widget(self.wrapped_button)
        else:
            if self.wrapped_button not in self.content.children:
                self.content.add_widget(self.wrapped_button)

        self.message.text = self._prep_text(correct)

        super(MathPopup, self).open()
        if correct:
            Clock.schedule_once(self.dismiss, 1)

    def _prep_text(self, correct):
        if correct:
            index = random.randint(0, len(self.GOOD_LIST) - 1)
            return self.GOOD.format(self.GOOD_LIST[index])
        else:
            index = random.randint(0, len(self.BAD_LIST) - 1)
            math_screen = App.get_running_app().root.math_screen
            answer = math_screen.get_answer()
            return self.BAD.format(self.BAD_LIST[index], answer)

###############################################################################
class KeyPad(GridLayout):

    def __init__(self, *args,**kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)
        self.cols = 3
        self.spacing = 10
        self.createButtons()

    def createButtons(self):
        button_lst = [7, 8, 9, 4, 5, 6, 1, 2, 3, "", 0, "Answer"]
        for button in button_lst:
            self.add_widget(Button(text=str(button), on_release=self.onBtnPress))

    def onBtnPress(self, btn):
        math_screen = App.get_running_app().root.ids.math_screen
        answer_text = math_screen.answer_text

        if btn.text.isdigit():
            answer_text.text += btn.text
            
        if btn.text == "Answer" and answer_text.text != "":
            answer = math_screen.get_answer()
            root = App.get_running_app().root
            if int(answer_text.text) == answer:
                root.math_popup.open(True)
            else:
                root.math_popup.open(False)

            answer_text.text = ""

            question = math_screen.question_text
            question.text = root.prepQuestion(
                math_screen.get_next_question(True if root.is_mix else False)
            )

###############################################################################

class KivyTutorApp(App):
    """App object
    """

    def __init__(self, **kwargs):
        super(KivyTutorApp, self).__init__(**kwargs)
        self.use_kivy_settings = False
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        # user presses back button
        if key == 32:
            return self.root.onBackBtn()


    def build(self):
        self.icon = "./images/testlogo.png"
        return MathPuzzleRoot()

    def getText(self):
        return ("\nHello world!\n"
                "This is Math-puzzle project of 03-01\n"
                "\nKamolchanok  Chuchuen    6410110005\n"
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