from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def handle_greet(self):
        """Read name and show greeting in the yellow label."""
        name = self.root.ids.input_name.text.strip()
        self.root.ids.output_label.text = f"Hello {name or 'world'}"

    def handle_clear(self):
        """Clear both the input field and the output label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
