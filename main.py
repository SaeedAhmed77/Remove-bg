from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from remove_bg_api import RemoveBg
import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Remove_Bg(MDApp):
    loadfile = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def build(self):
        return Builder.load_file("main.kv")

    def file_chooser(self):
        content = LoadDialog(load = self.selected, cancel = self.dismiss_popup)
        self._popup = Popup(title = "Load file", content = content,
                            size_hint = (0.9, 0.9), auto_dismiss = False)
        self._popup.open()

    def selected(self, filename):
        if filename:
            self.root.ids.img.source = filename[0]
            self.dismiss_popup()

    def remove_bg(self, save_as, extension):
        remove_bg = RemoveBg("ypxnpGwExzTqanyghpgz48rN")
        if remove_bg.remove_bg_file(input_path = self.root.ids.img.source, out_path = save_as+"."+extension, size = "preview", raw = False):
            toast("The mission was completed, thank you for using this app", 5)

    def validation(self):
        toast("You must fill all the fields!", 5)

Factory.register('LoadDialog', cls=LoadDialog)
if __name__ == "__main__":
    Remove_Bg().run()