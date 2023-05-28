from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<MD3Card>
    padding: 10
    size_hint: None, None
    size: "400dp", "500dp"

    MDRelativeLayout:
        orientation: 'vertical'
    
        MDLabel:
            id: label
            text: root.text
            pos_hint:  {'center_x': 0.5, 'y': 0.9}
            adaptive_size: True
            color: "grey"
            bold: True
            
        MDGridLayout:
            pos_hint:  {'x': 0, 'y': 0}
            size_hint_y: None
            row_default_height: 10
            cols: 2
            padding: 10
            spacing: 10
        
            MDRaisedButton:
                text: "Мир"
                size_hint: 1, 1
            MDRaisedButton:
                text: "Даждьбог"
                size_hint: 1, 1
            MDRaisedButton:
                text: "Исток"
                size_hint: 1, 1
            MDRaisedButton:
                text: "Леля"
                size_hint: 1, 1


MDScreen:
    MDBoxLayout:
        id: box
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class MD3Card(MDCard):
    text = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.box.add_widget(
            MD3Card(
                line_color=(0.1, 0.1, 0.1, 0),
                style="elevated",
                text="Какая руна здесь изображена?",
                md_bg_color="#f6eeee",
                shadow_softness=20,
                shadow_offset=(0, 5),
            )
        )


Example().run()
