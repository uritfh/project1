from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

kv_code = '''
BoxLayout:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '10dp'
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDTextField:
        id: lot_size_input
        hint_text: "Enter amount in Dollars you want to be rewarded per pip ($)"
        input_filter: "float"
        helper_text_mode: "on_focus"
        helper_text: "Do it the Urich way!."

    MDRaisedButton:
        text: "Convert to Lot size"
        on_press: app.convert_lot_to_dollars()

    MDLabel:
        id: result_label
        halign: 'center'
'''

class LotConverterApp(MDApp):
    def build(self):
        return Builder.load_string(kv_code)

    def convert_lot_to_dollars(self):
        try:
            lot_size = float(self.root.ids.lot_size_input.text)
            dollar_amount = lot_size * 0.10  # Assuming 1 lot equals 0.10$
            result_label = self.root.ids.result_label
            result_label.text = f"Risking per pip: {lot_size} $ is equal to {dollar_amount:.2f} Lot"
        except ValueError:
            result_label = self.root.ids.result_label
            result_label.text = "Invalid input. Please enter a valid lot size."

if __name__ == '__main__':
    LotConverterApp().run()
