from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exemples.kv")

class WidgetsExemple(GridLayout):
    ActiveBool = BooleanProperty(False)
    compteur = 1
    mon_texte = StringProperty("1")
    # slider_value_txt = StringProperty("0")
    text_input_str = StringProperty("toto")

    def on_button_click(self):
        print("Button click")
        if self.ActiveBool:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_toggle_button_state(self,widget):
        print("Toggle state : " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.ActiveBool = False
        else:
            widget.text = "ON"
            self.ActiveBool =True

    def on_switch_active(self, widget):
        print("Switch " + str(widget.active))

    def on_Slider_Change(self, widget):
        print("Slider : " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text