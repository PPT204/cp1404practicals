from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """App that dynamically creates labels from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is our data (model)
        self.names = ["Jordan", "Alice", "Bob", "Charlie"]

    def build(self):
        """Build the GUI and dynamically add labels."""
        self.root = Builder.load_file("dynamic_labels.kv")

        # Add one Label for each name
        for name in self.names:
            temp_label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(temp_label)

        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()
