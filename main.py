from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from datetime import datetime

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)

class MainApp(MDApp):
    task_list_dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
                size_hint=(0.8, 0.8),
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="Cancel",
                        on_release=self.task_list_dialog.dismiss
                    ),
                    MDRaisedButton(
                        text="Add",
                        on_release=self.add_task_function
                    )
                ]
            )
            self.task_list_dialog.open()

    def add_task_function(self, *args):
        task_content = self.task_list_dialog.content_cls
        task = task_content.ids.task_text.text
        task_date = task_content.ids.date_text.text
        self.task_list_dialog.dismiss()
        print(task, task_date)

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

if __name__ == "__main__":
    app = MainApp()
    app.run()

