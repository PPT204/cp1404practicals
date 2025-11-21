from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesKmApp(App):
    km_output = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file("convert_miles_km.kv")

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0

        km = miles * MILES_TO_KM
        self.km_output = str(round(km, 5))

    def handle_increment(self, amount):
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0
        value += amount
        self.root.ids.input_miles.text = str(value)

if __name__ == "__main__":
    MilesKmApp().run()
