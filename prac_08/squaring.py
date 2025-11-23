"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'

class SquareNumberApp(App):
    """Square Number 2 – squares the given input text."""

    def build(self):
        self.title = "Square Number 2"
        return Builder.load_file("squaring.kv")

    def handle_calculate(self, text):
        """Square the value in text and show the result."""
        try:
            number = float(text)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid"


SquareNumberApp().run()
