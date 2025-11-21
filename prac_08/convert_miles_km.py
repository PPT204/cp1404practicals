from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesKmApp(App):
    km_output = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file("convert_miles_km.kv")

if __name__ == "__main__":
    MilesKmApp().run()
