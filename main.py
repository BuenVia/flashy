from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from word_list import word_list

class MainLayout(BoxLayout):
    index = 0
    word = word_list[index]
    display_word = StringProperty(word["eng"])
    display_lang = StringProperty("English")
    display_number = StringProperty(f"{index + 1} / {len(word_list)}")

    def flip(self):
        if self.display_word == self.word["eng"]:
            self.display_word = self.word["spa"]
            self.display_lang = "Spanish"
        else:
            self.display_word = self.word["eng"]
            self.display_lang = "English"

    def next(self):
        if self.index < len(word_list) - 1:
            self.index += 1
            self.word = word_list[self.index]
            self.display_word = self.word["eng"]
            self.display_number = f"{self.index + 1} / {len(word_list)}"
        else:
            self.index = 0
            self.word = word_list[self.index]
            self.display_word = self.word["eng"]
            self.display_number = f"{self.index + 1} / {len(word_list)}"

    def bg_color(self):
        if self.display_lang == "Spanish":
            return (0, 1, 0)
        else:
            return (1, 0, 0)

class MainApp(App):
    pass

if __name__ == "__main__":
    MainApp().run()