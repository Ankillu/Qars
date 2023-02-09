from kivymd.app import MDApp
from kivy.lang import Builder

class Qars(MDApp):
    def build(self):
        self.root = Builder.load_file('qars.kv')
        return self.root

if __name__ == '__main__':
    Qars().run()
