from kivy.app import App

from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.dropdown import DropDown

from kivy.graphics import Rectangle, Color, RoundedRectangle
from kivy.properties import NumericProperty

from kivy.core.window import Window
from kivy.clock import Clock

from kivy.config import Config, ConfigParser
from kivy.animation import Animation
from kivy.metrics import dp

from datetime import datetime, timedelta

import os
import ast
import math

Config.set("graphics", "fullscreen", False)
Config.write()
Config.set("graphics", "resizable", "1")  # для того чтоб гловное окно не изменялось
Config.set("graphics", "width", "350")  # widht main_window
Config.set("graphics", "height", "650")  # heigth main_window
Config.write()

# Config.set('kivy', 'exit_on_escape', '0')

# Тим, що ви вимкнете компютер, а не залишите його в сплячому режимі, ви можете заощадити до 40 ват електроенергії на добу. Якщо ви не хочете вранці чекати завантаження компютера, то чому б йому не завантажуватися поки ви вмиваєтеся? Або ж можна поставити його на автоматичне включення вранці. Те ж саме стосується й інших електричних приладів - краще все вимкнути повністю.

actions_english = [
    ["легкий", 0],
    # -----------------
    # ["Вимикати компьютер наніч", "none"],
    # ["Використовувати папір для друку зобох сторін", "none"],
    # ["Здавати скло на переробку", "none"],
    # ["Сушити речі на мотузці", "none"],
    # ["Вимикати світло, коли виходиш з кімнати", "none"],
    # ["Здавати папір та картон на переробку", "none"],
    # ["Здавати пластик на переробку", "none"],
    # ["Здавати батарейки на переробку", "none"],
    # ["Здавати метал на переробку", "none"],
    # ["Купувати менше напоїв в пластикових пляшках", "none"],
    # ["Відмовитись від поліетиленових пакетів", "none"],
    # ["Закривати воду, коли чистиш зуби", "none"],
    # ["Віддати перевагу місцевим товарам", "none"],
    # ["Ефективно використовуйте кондиціонер та обігрівач", "none"],
    # ["Комбінуйте поїздки у справах", "none"],
    # ["Звертайте увагу на упаковку", "none"],
    # ["Віддавайте старі мобільні телефони на переробку", "none"],
    # ["Віддавайте непотрібні речі", "none"],
    # ["Відключайте зарядний пристрій", "none"],
    # ["Ходіть пішки", "none"],
    # ["Платіть за рахунками онлайн", "none"],
    # -----------------
    ["Turn off computer at night", "none"],
    ["Use paper to print both sides", "none"],
    ["Give glass for recycling", "none"],
    ["Dry things on a line", "none"],
    ["Turn off the light when you leave the room", "none"],
    ["Send paper and cardboard for recycling", "none"],
    ["Give plastic for recycling", "none"],
    ["Recycle batteries", "none"],
    ["Give metal for recycling", "none"],
    ["Buy fewer drinks in plastic bottles", "none"],
    ["Abandon plastic bags", "none"],
    ["Turn off the water when you brush your teeth", "none"],
    ["Prefer local products", "none"],
    ["Use the air conditioner and heater efficiently", "none"],
    ["Combine business trips", "none"],
    ["Pay attention to the packaging", "none"],
    ["Recycle old mobile phones", "none"],
    ["Give away unnecessary items", "none"],
    ["Disconnect charger", "none"],
    ["Walk", "none"],
    ["Pay bills online", "none"],
    # -----------------
    ["сложний", 1],
    # -----------------
    # ["Замінити лампу на енергозберігаючу", "none"],
    # ["Полагодьте труби та крани", "none"],
    # ["Посадіть дерево", "none"],
    # ["Підтримуйте ваш автомобіль в хорошому стані", "none"],
    # ["Вирощувати кімнатні рослини", "none"],
    # ["Використовуати сірники замість запальнички", "none"],
    # ["Використовуйте ганчіркові серветки", "none"],
    # ["Підвезіть колегу", "none"],
    # ["Використовуйте акумуляторні батареї", "none"],
    # ["Використовувати екосумку", "none"],
    # ["Використовуйте багаторазову пляшку", "none"],
    # ["Використовуйте багаторазову чашку", "none"],
    # ["Використовуйте багаторазовий ланч-бокс", "none"],
    # ["Використовуйте бамбукову щітку", "none"],
    # ["Відмовтесь від одноразових станків для гоління", "none"],
    # ["Облаштуйте дома контейнери для сортування сміття", "none"],
    # ["Встановіть аератор на кран", "none"],
    # -----------------
    ["Replace the lamp with an energy-saving one", "none"],
    ["Fix pipes and faucets", "none"],
    ["Plant a tree", "none"],
    ["Keep your car in good condition", "none"],
    ["Grow indoor plants", "none"],
    ["Use matches instead of lighters", "none"],
    ["Use rag wipes", "none"],
    ["Give a ride to a colleague", "none"],
    ["Use rechargeable batteries", "none"],
    ["Use ecobag", "none"],
    ["Use a reusable bottle", "none"],
    ["Use a reusable cup", "none"],
    ["Use a reusable lunch box", "none"],
    ["Use a bamboo brush", "none"],
    ["Abandon disposable razors", "none"],
    ["Set up waste sorting containers at home", "none"],
    ["Install the aerator on the faucet", "none"],
    # -----------------
    ["про", 2],
    # -----------------
    # ["Обирати енергозберігаючу побутову техніку", "none"],
    # ["Користуватись екологічною побутовою хімією", "none"],
    # ["Їздити на велосипеді", "none"],
    # ["Купити гарний керамічний набір для пікнику", "none"],
    # ["Обрати електромобіль", "none"],
    # ["Встановити вітрогенератор", "none"],
    # ["Встановити сонячні батареї", "none"],
    # -----------------
    ["Choose energy-saving household appliances", "none"],
    ["Use ecological household chemicals", "none"],
    ["Ride a bike", "none"],
    ["Buy a nice ceramic picnic set", "none"],
    ["Choose an electric car", "none"],
    ["Install Wind Generator", "none"],
    ["Install solar panels", "none"],
    # -----------------
]

actions = [
    ["легкий", 0],
    # -----------------
    ["Вимикати компьютер наніч", "none"],
    ["Використовувати папір для друку зобох сторін", "none"],
    ["Здавати скло на переробку", "none"],
    ["Сушити речі на мотузці", "none"],
    ["Вимикати світло, коли виходиш з кімнати", "none"],
    ["Здавати папір та картон на переробку", "none"],
    ["Здавати пластик на переробку", "none"],
    ["Здавати батарейки на переробку", "none"],
    ["Здавати метал на переробку", "none"],
    ["Купувати менше напоїв в пластикових пляшках", "none"],
    ["Відмовитись від поліетиленових пакетів", "none"],
    ["Закривати воду, коли чистиш зуби", "none"],
    ["Віддати перевагу місцевим товарам", "none"],
    ["Ефективно використовуйте кондиціонер та обігрівач", "none"],
    ["Комбінуйте поїздки у справах", "none"],
    ["Звертайте увагу на упаковку", "none"],
    ["Віддавайте старі мобільні телефони на переробку", "none"],
    ["Віддавайте непотрібні речі", "none"],
    ["Відключайте зарядний пристрій", "none"],
    ["Ходіть пішки", "none"],
    ["Платіть за рахунками онлайн", "none"],
    # -----------------
    # ["Turn off computer at night", "none"],
    # ["Use paper to print both sides", "none"],
    # ["Give glass for recycling", "none"],
    # ["Dry things on a line", "none"],
    # ["Turn off the light when you leave the room", "none"],
    # ["Send paper and cardboard for recycling", "none"],
    # ["Give plastic for recycling", "none"],
    # ["Recycle batteries", "none"],
    # ["Give metal for recycling", "none"],
    # ["Buy fewer drinks in plastic bottles", "none"],
    # ["Abandon plastic bags", "none"],
    # ["Turn off the water when you brush your teeth", "none"],
    # ["Prefer local products", "none"],
    # ["Use the air conditioner and heater efficiently", "none"],
    # ["Combine business trips", "none"],
    # ["Pay attention to the packaging", "none"],
    # ["Recycle old mobile phones", "none"],
    # ["Give away unnecessary items", "none"],
    # ["Disconnect charger", "none"],
    # ["Walk", "none"],
    # ["Pay bills online", "none"],
    # -----------------
    ["сложний", 1],
    # -----------------
    ["Замінити лампу на енергозберігаючу", "none"],
    ["Полагодьте труби та крани", "none"],
    ["Посадіть дерево", "none"],
    ["Підтримуйте ваш автомобіль в хорошому стані", "none"],
    ["Вирощувати кімнатні рослини", "none"],
    ["Використовуати сірники замість запальнички", "none"],
    ["Використовуйте ганчіркові серветки", "none"],
    ["Підвезіть колегу", "none"],
    ["Використовуйте акумуляторні батареї", "none"],
    ["Використовувати екосумку", "none"],
    ["Використовуйте багаторазову пляшку", "none"],
    ["Використовуйте багаторазову чашку", "none"],
    ["Використовуйте багаторазовий ланч-бокс", "none"],
    ["Використовуйте бамбукову щітку", "none"],
    ["Відмовтесь від одноразових станків для гоління", "none"],
    ["Облаштуйте дома контейнери для сортування сміття", "none"],
    ["Встановіть аератор на кран", "none"],
    # -----------------
    # ["Replace the lamp with an energy-saving one", "none"],
    # ["Fix pipes and faucets", "none"],
    # ["Plant a tree", "none"],
    # ["Keep your car in good condition", "none"],
    # ["Grow indoor plants", "none"],
    # ["Use matches instead of lighters", "none"],
    # ["Use rag wipes", "none"],
    # ["Give a ride to a colleague", "none"],
    # ["Use rechargeable batteries", "none"],
    # ["Use ecobag", "none"],
    # ["Use a reusable bottle", "none"],
    # ["Use a reusable cup", "none"],
    # ["Use a reusable lunch box", "none"],
    # ["Use a bamboo brush", "none"],
    # ["Abandon disposable razors", "none"],
    # ["Set up waste sorting containers at home", "none"],
    # ["Install the aerator on the faucet", "none"],
    # -----------------
    ["про", 2],
    # -----------------
    ["Обирати енергозберігаючу побутову техніку", "none"],
    ["Користуватись екологічною побутовою хімією", "none"],
    ["Їздити на велосипеді", "none"],
    ["Купити гарний керамічний набір для пікнику", "none"],
    ["Обрати електромобіль", "none"],
    ["Встановити вітрогенератор", "none"],
    ["Встановити сонячні батареї", "none"],
    # -----------------
    # ["Choose energy-saving household appliances", "none"],
    # ["Use ecological household chemicals", "none"],
    # ["Ride a bike", "none"],
    # ["Buy a nice ceramic picnic set", "none"],
    # ["Choose an electric car", "none"],
    # ["Install Wind Generator", "none"],
    # ["Install solar panels", "none"],
    # -----------------
]

language = ["UA", "UK"]

only_actions = []

# wat = ("1Ват.", "2Ват.", "5Ват.", "15Ват.", "30Ват.")
# kg = ("1кг.", "5кг.", "10кг.", "20кг.", "40кг.")
# lit = ("1л.", "2л.", "5л.", "10л.", "20л.")
wat = ("1 Watt.", "2 Watt.", "5 Watt.", "15 Watt.", "30 Watt.")
kg = ("1kg.", "5kg.", "10kg.", "20kg.", "40kg.")
lit = ("1l.", "2l.", "5l.", "10l.", "20l.")

# value_time = ["1 день", "2 дні", "3 дні", "1 неділля", "2 неділлі", "3 неділлі"]
value_time = ["1 day", "2 days", "3 days", "1 Sunday", "2 Sundays", "3 Sundays"]
value_t = [
    3600 * 24,
    3600 * 24 * 2,
    3600 * 24 * 3,
    3600 * 24 * 7,
    3600 * 24 * 7 * 2,
    3600 * 24 * 7 * 3,
]

# valume = ["Гучність музики", "Гучність спец ефектів"]
valume = ["Music volume", "Volume of special effects"]

if Window.size[0] >= 450:
    font_size_all = 24
elif Window.size[0] >= 350:
    font_size_all = 19
elif Window.size[0] <= 320:
    font_size_all = 15


class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            Rectangle(
                pos=(0, 0),
                size=Window.size,
                source=".\\image\\good.jpg",
            )

            Color(0, 0, 0, 0.4)
            Rectangle(pos=(0, 0), size=Window.size)

    def on_enter(self):
        self.box = BoxLayout(orientation="vertical", padding=(0, 50), spacing=10)
        box_small_menu = BoxLayout(
            orientation="vertical", padding=(50, 20), size_hint=(1, 0.2), spacing=10
        )

        with open(".\\language.txt", "r") as file:
            for line in file:
                language_image = str(line)

        self.box.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\main_logo.svg",
                source=f".\\{language_image}\\main_logo.png",
                size_hint=(1, None),
                height=150,
            )
        )
        self.box.add_widget(
            Image(
                source=".\\image\\green_earch.png",
                size_hint=(1, None),
                height=200,
            )
        )
        box_small_menu.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\menu_list.png",
                source=f".\\{language_image}\\myCheckList.png",
                on_press=lambda x: set_screen("check_list"),
                size_hint=(1, None),
                height=50,
            )
        )
        box_small_menu.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\menu_add.png",
                source=f".\\{language_image}\\menu_add.png",
                on_press=lambda x: set_screen("add_check_list"),
                size_hint=(1, None),
                height=50,
            )
        )
        self.box.add_widget(box_small_menu)
        self.add_widget(self.box)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана
        self.box.clear_widgets()  # очищаем список


class MyCheckList(Screen):
    height_headerfooter = 75
    time_zero = 0
    main_value = 0
    scroll_distance_list_y = 1

    time_again = timedelta(seconds=value_t[0])

    state_btn_start = NumericProperty(0)
    a = NumericProperty(value_t[0])
    eco_mide = NumericProperty(0)
    b = NumericProperty(10)

    time_1 = timedelta(hours=0, minutes=0, seconds=value_t[0])

    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            Rectangle(
                pos=(0, 0),
                size=Window.size,
                source=".\\image\\good.jpg",
            )

            Color(0, 0, 0, 0.4)
            Rectangle(pos=(0, 0), size=Window.size)

        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(
                pos=(0, Window.size[1] - self.height_headerfooter),
                size=(Window.size[0], self.height_headerfooter),
            )
            RoundedRectangle(
                pos=(0, 0),
                size=(Window.size[0], self.height_headerfooter),
                radius=[(20.0, 20.0), (20.0, 20.0), (0.0, 0.0), (0.0, 0.0)],
            )

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        indx_remove = 0

        self.app = App.get_running_app()
        self.app.user_data2 = ast.literal_eval(
            self.app.config.get("General", "user_data2")
        )
        if "State" not in self.app.user_data2:
            self.app.user_data2["State"] = self.state_btn_start
        elif self.app.user_data2["State"] == 2:
            self.state_btn_start = self.app.user_data2["State"]
        elif self.app.user_data2["State"] == 1:
            self.state_btn_start = self.app.user_data2["State"]
        elif self.state_btn_start == 1 or self.state_btn_start == 0:
            self.app.user_data2["State"] = self.state_btn_start
        else:
            self.state_btn_start = self.app.user_data2["State"]

        self.app.config.set("General", "user_data2", self.app.user_data2)
        self.app.config.write()

        self.dic_foods = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data")
        )

        l = len(self.dic_foods.items())

        self.main = BoxLayout(orientation="vertical")

        header = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=self.height_headerfooter,
            spacing=5,
        )
        self.footer = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=75,
            padding=(10, 10, 10, 10),
        )

        self.layout = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        back_button = Btn(
            size_hint=(None, 1),
            source=".\\image\\back.png",
            width=50,
        )
        back_button.bind(on_press=self.back_button_press_now)
        timer = Btn(size_hint=(0.2, 1), source=".\\image\\timer.png")
        timer.bind(on_press=self.timer_press)
        if l == 0:
            self.start_button = Btn(size_hint=(0.6, 1))
        elif self.state_btn_start == 1:
            self.start_button = Btn(
                # size_hint=(0.6, 1), source="F:\\python\\kivyProjects\\image\\result.png"
                size_hint=(0.6, 1),
                source=f".\\{get_language_now()}\\result.png",
            )
            self.start_button.bind(on_press=self.result_now)
            self.footer.add_widget(timer)
            self.footer.add_widget(self.start_button)
        elif self.state_btn_start == 0 and l > 0:
            self.start_button = Btn(size_hint=(0.6, 1), source=".\\image\\st.png")
            self.start_button.bind(on_press=self.btn_start_press)
            self.footer.add_widget(timer)
            self.footer.add_widget(self.start_button)
        else:
            self.start_button = Btn(
                size_hint=(0.6, 1),
                # source="F:\\python\\kivyProjects\\image\\res_now.png",
                source=f".\\{get_language_now()}\\res_now.png",
            )
            self.start_button.bind(on_press=self.result_press)
            self.footer.add_widget(timer)
            self.footer.add_widget(self.start_button)

        settings = Btn(size_hint=(0.2, 1), source=".\\image\\opt.png")
        settings.bind(on_press=self.setting_press)

        self.root = ScrollView(scroll_y=self.scroll_distance_list_y)

        self.state = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data2")
        )
        self.time_text = ast.literal_eval(
            App.get_running_app().config.get("General", "time_txt")
        )

        header.add_widget(back_button)
        header.add_widget(Label(size_hint=(None, 1), width=10))
        img_head = BoxLayout(
            orientation="horizontal", size_hint=(0.7, 1), padding=(10, 10)
        )
        img_head.add_widget(
            Image(
                # source="F:\\python\\kivyProjects\\image\\mini_logo.png",
                source=f".\\{get_language_now()}\\image.png",
                size_hint=(1, 1),
            )
        )
        header.add_widget(img_head)
        self.label_clock = Label(
            size_hint=(None, 1),
            text=f"{timedelta(seconds=self.time_text[0])}",
            width=60,
            text_size=(60, None),
            color=(122 / 255, 170 / 255, 28 / 255, 1),
            halign="center",
        )

        self.time_1 = timedelta(seconds=self.time_text[0])

        self.a = self.time_1.seconds + self.time_1.days * 3600 * 24

        if self.state["State"] == 2:
            self.label_clock.text = ""
        header.add_widget(self.label_clock)

        st = ast.literal_eval(App.get_running_app().config.get("General", "user_data2"))

        if st["State"] == 1:
            self.time_now()

        self.root.add_widget(self.layout)

        self.footer.add_widget(settings)

        self.main.add_widget(header)
        if l == 0:
            box_for_zero = BoxLayout(orientation="vertical")
            box_for_zero_small = BoxLayout(
                orientation="horizontal", size_hint=(1, 0.24)
            )
            box_for_zero.add_widget(Label(size_hint=(1, 0.33)))
            if get_language_now() == "image":
                x = "Щоб почати, натисни кнопку нижче"
            else:
                x = "Click the button below to get started"
            box_for_zero.add_widget(
                Label(
                    # text="Щоб почати, натисни кнопку нижче",
                    text=x,
                    halign="center",
                    text_size=(Window.size[0] - 20, None),
                    font_size=20,
                    size_hint=(1, 0.1),
                )
            )
            btn_zero = Btn(
                # source="F:\\python\\kivyProjects\\image\\button_add.png",
                source=f".\\{get_language_now()}\\button_add.png",
                size_hint=(0.4, 1),
            )
            btn_zero.bind(on_press=self.back_button_press_now)
            box_for_zero_small.add_widget(Label(size_hint=(0.3, 1)))
            box_for_zero_small.add_widget(btn_zero)
            box_for_zero_small.add_widget(Label(size_hint=(0.3, 1)))
            box_for_zero.add_widget(box_for_zero_small)
            box_for_zero.add_widget(Label(size_hint=(1, 0.33)))
            self.main.add_widget(box_for_zero)
        else:
            self.main.add_widget(self.root)
        self.main.add_widget(self.footer)

        self.add_widget(self.main)

        for f, d in self.dic_foods.items():
            test = BoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(50),
                padding=(10, 5),
            )
            if d != "none":
                fd = f + " " + str(d)
            else:
                fd = f

            btn = Label(
                text=fd,
                size_hint=(0.8, 1),
                text_size=(Window.size[0] - 70, None),
                halign="center",
                padding=(10, 10),
                font_size=font_size_all,
                color=(1, 1, 1),
            )
            btn2 = Btn_remove(
                size_hint=(None, 1),
                source=".\\image\\rem_green.png",
                width=50,
            )
            btn2.n_remove = indx_remove
            btn2.bind(on_press=self.btn_press)
            check_btn = MyButton_check(size_hint=(0.2, 1))
            check_btn.bind(on_press=self.checkbox_press)

            test.add_widget(btn)

            if self.state_btn_start == 0:
                test.add_widget(btn2)
            elif self.state_btn_start == 2:
                test.add_widget(check_btn)

            self.layout.add_widget(test)

            indx_remove += 1

    def on_leave(self):  # Будет вызвана в момент закрытия экрана
        self.layout.clear_widgets()  # очищаем список

        self.main.clear_widgets()

    def update_all(self):
        self.footer.clear_widgets()

    def result_now(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.a = 1
        self.time_1 = timedelta(seconds=self.a)
        self.start()

    def time_now(self):
        if self.main_value == 0:
            user_data4 = ast.literal_eval(
                App.get_running_app().config.get("General", "user_data4")
            )
            time_now = datetime.now()
            time_past = datetime(
                year=user_data4[0][0],
                month=user_data4[0][1],
                day=user_data4[0][2],
                hour=user_data4[0][3],
                minute=user_data4[0][4],
                second=user_data4[0][5],
            )

            time_sum = time_past + timedelta(seconds=user_data4[0][6])

            if time_sum <= time_now:
                self.main_value = 1
                self.a = 4
                self.time_1 = timedelta(seconds=self.a)
                self.start()

            else:
                des = time_sum - time_now
                des_back = timedelta(seconds=user_data4[0][6]) - des
                des_non = timedelta(seconds=user_data4[0][6]) - des_back
                self.a = des_non.seconds + des_non.days * 3600 * 24

                self.time_1 = timedelta(seconds=self.a)

                self.start()

    def back_button_press_now(self, instance):
        self.on_leave()
        self.update_all()
        self.scroll_distance_list_y = self.root.scroll_y
        # if instance.source == "F:\\python\\kivyProjects\\image\\button_add.png":
        if instance.source == f".\\{get_language_now()}\\button_add.png":
            set_screen("add_check_list")
        else:
            set_screen("menu")

    def btn_press(self, bt):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get("General", "user_data")
        )

        self.app.user_data3 = ast.literal_eval(
            self.app.config.get("General", "user_data3")
        )

        del self.app.user_data[self.app.user_data3[bt.n_remove]]
        self.app.user_data3.pop(bt.n_remove)

        self.app.config.set("General", "user_data3", self.app.user_data3)
        self.app.config.write()

        self.app.config.set("General", "user_data", self.app.user_data)
        self.app.config.write()

        self.on_leave()
        self.update_all()
        self.on_enter()

    def btn_start_press(self, bt):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.main_value = 1
        self.state_btn_start = 1

        user_data2 = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data2")
        )
        user_data2["State"] = self.state_btn_start

        self.app.config.set("General", "user_data2", user_data2)
        self.app.config.write()

        user_data4 = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data4")
        )
        time_zero_now = datetime.now()
        user_data4.append(
            [
                time_zero_now.year,
                time_zero_now.month,
                time_zero_now.day,
                time_zero_now.hour,
                time_zero_now.minute,
                time_zero_now.second,
                self.a,
            ]
        )

        self.app.config.set("General", "user_data4", user_data4)
        self.app.config.write()

        self.update_all()
        self.on_leave()
        self.on_enter()

        self.start()

    def start(self):
        user_data2 = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data2")
        )
        if user_data2["State"] != 2:
            Animation.cancel_all(self)  # stop any current animations
            self.anim = Animation(a=0, duration=self.a)

            def finish_callback(animation, incr_crude_clock):
                incr_crude_clock.text = "FINISHED"

            self.anim.bind(on_complete=finish_callback)
            self.anim.start(self)

    def on_a(self, instance, value):
        state_time = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data2")
        )

        if state_time["State"] == 1:
            self.text = str(round(value, 1))
            if self.text == f"{int(round(value, 1))}.0" and self.text != self.time_zero:
                self.time_zero = self.text
                time_2 = timedelta(seconds=1)
                self.time_1 = self.time_1 - time_2
            self.label_clock.text = f"{self.time_1}"
            if self.text == "0.0":
                self.app = App.get_running_app()
                self.app.user_data2 = ast.literal_eval(
                    self.app.config.get("General", "user_data2")
                )
                self.app.user_data2["State"] = 2

                self.app.config.set("General", "user_data2", self.app.user_data2)
                self.app.config.write()
                self.on_leave()
                self.update_all()
                self.on_enter()

    def checkbox_press(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        actions = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data3")
        )
        len_act = 100 / len(actions)

        if instance.state_checkbox == 0:
            instance.source = ".\\image\\checkbox_ok.png"
            instance.state_checkbox = 1
            self.eco_mide += len_act
        else:
            instance.source = ".\\image\\checkbox_no.png"
            instance.state_checkbox = 0
            self.eco_mide -= len_act

    def result_press(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        self.sound = SoundLoader.load(".\\music\\fanfar.mp3")
        self.sound.volume = self.app.user_data7[1]
        self.sound.play()
        user_data4 = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data4")
        )
        user_data4.pop(0)

        self.app.config.set("General", "user_data4", user_data4)
        self.app.config.write()
        btn_popup = Btn(size_hint=(1, 0.65))
        self.eco_mide = math.trunc(self.eco_mide)

        if get_language_now() == "image":
            x = "Непогано! Кожен крок наближає нас до чистого міста! Разом зробимо ще більше для нашого здорового майбутнього!"
            y = "Дуже добре! Кожна дія зменшує твій особистий екологічний слід та зменшує навантаження на екологію міста!"
            z = "Молодець! Так тримати! Місто тобі дякує!"
        else:
            x = "Not bad! Every step brings us closer to a clean city! Let's do more together for our healthy future!"
            y = "Very good! Every action reduces your personal ecological footprint and reduces the burden on the city's ecology!"
            z = "Well done! Keep it up! The city thanks you!"
        if self.eco_mide < 40:
            btn_popup.source = ".\\image\\eco_krock.png"
            # txt = "Непогано! Кожен крок наближає нас до чистого міста! Разом зробимо ще більше для нашого здорового майбутнього!"
            txt = x
        elif self.eco_mide < 70:
            btn_popup.source = ".\\image\\result_planet.jpg"
            # txt = "Дуже добре! Кожна дія зменшує твій особистий екологічний слід та зменшує навантаження на екологію міста!"
            txt = y
        else:
            btn_popup.source = ".\\image\\zero_city.webp"
            # txt = "Молодець! Так тримати! Місто тобі дякує!"
            txt = z

        box_age = BoxLayout(orientation="vertical", padding=(5, 5))
        box_age.add_widget(btn_popup)
        self.pb = ProgressBar(max=100.0, size_hint=(1, 0.1))
        box_age.add_widget(self.pb)
        box_age.add_widget(
            Label(
                # text=f"{txt}\nТвій результат: {math.trunc(self.eco_mide)}%",
                text=f"{txt}\nYour result: {math.trunc(self.eco_mide)}%",
                color=(122 / 255, 170 / 255, 28 / 255, 1),
                size_hint=(1, 0.1),
                halign="center",
                text_size=(Window.size[0] - 30, None),
            )
        )
        box_age_small = BoxLayout(orientation="horizontal", size_hint=(1, 0.12))
        btn_back = Btn(source=".\\image\\btn_ok.png", size_hint=(0.3, 1))
        btn_back.bind(on_press=self.btn_back_press)
        box_age.add_widget(Label(size_hint=(1, 0.03)))
        box_age_small.add_widget(Label(size_hint=(0.35, 1)))
        box_age_small.add_widget(btn_back)
        box_age_small.add_widget(Label(size_hint=(0.35, 1)))
        box_age.add_widget(box_age_small)

        if get_language_now() == "image":
            x = "Мій результат"
        else:
            x = "My result"
        self.popup = Popup(
            # title="Мій результат",
            title=x,
            content=box_age,
            padding=(10, 0),
            size_hint=(1, None),
            height=Window.size[1] - 100,
            separator_color=(122 / 255, 170 / 255, 28 / 255, 1),
            title_align="center",
            title_color=(122 / 255, 170 / 255, 28 / 255, 1),
        )
        self.popup.open()
        self.start2()
        self.app = App.get_running_app()
        self.app.user_data2 = ast.literal_eval(
            self.app.config.get("General", "user_data2")
        )

        self.app.user_data2["State"] = 0

        self.app.config.set("General", "user_data2", self.app.user_data2)
        self.app.config.write()

        self.app.user_data = ast.literal_eval(
            self.app.config.get("General", "user_data")
        )

        self.app.user_data.clear()

        self.app.config.set("General", "user_data", self.app.user_data)
        self.app.config.write()

        self.app.user_data3 = ast.literal_eval(
            self.app.config.get("General", "user_data3")
        )

        self.app.user_data3.clear()

        self.app.config.set("General", "user_data3", self.app.user_data3)
        self.app.config.write()

        self.app.user_data6 = ast.literal_eval(
            self.app.config.get("General", "time_txt")
        )

        self.a = self.app.user_data6[0]
        self.time_1 = self.time_again

        self.on_leave()
        self.update_all()
        self.on_enter()

    def timer_press(self, instance):
        self.app = App.get_running_app()
        self.app.user_data2 = ast.literal_eval(
            self.app.config.get("General", "user_data2")
        )

        if self.app.user_data2 == 0 or self.state_btn_start == 0:
            box_timer_all = BoxLayout(orientation="vertical")
            box_timer = BoxLayout(
                orientation="vertical", spacing=10, padding=(20, 10), size_hint=(1, 0.8)
            )

            self.app = App.get_running_app()
            self.app.user_data7 = ast.literal_eval(
                self.app.config.get("General", "settings_value")
            )

            sound = SoundLoader.load(".\\music\\btn_press.mp3")
            sound.volume = self.app.user_data7[1]
            sound.play()

            for i in value_time:
                btn_timer = Button(
                    text=f"{i}",
                    background_color=(122 / 255, 170 / 255, 28 / 255, 1),
                    background_normal="",
                    font_size=(font_size_all + 5),
                )
                btn_timer.bind(on_press=self.timer_btn_press)
                box_timer.add_widget(btn_timer)

            box_timer_all.add_widget(box_timer)
            box_timer_all.add_widget(
                Btn(
                    # source="F:\\python\\kivyProjects\\image\\cansel.png",
                    source=f".\\{get_language_now()}\\cansel.png",
                    size_hint=(1, 0.2),
                    on_press=self.timer_back,
                )
            )

            if get_language_now() == "image":
                x = "Вибери час для виконання"
            else:
                x = "Choose a time to perform"
            self.popup_timer = Popup(
                # title="Вибери час для виконання",
                title=x,
                content=box_timer_all,
                padding=(10, 0),
                size_hint=(1, None),
                height=Window.size[1] - 100,
                separator_color=(122 / 255, 170 / 255, 28 / 255, 1),
                title_align="center",
                title_color=(122 / 255, 170 / 255, 28 / 255, 1),
            )

            self.popup_timer.open()

    def timer_btn_press(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()

        self.app = App.get_running_app()
        self.app.user_data6 = ast.literal_eval(
            self.app.config.get("General", "time_txt")
        )

        indx_time = value_time.index(instance.text)
        self.a = value_t[indx_time]
        self.time_1 = timedelta(seconds=value_t[indx_time])
        self.time_again = timedelta(seconds=value_t[indx_time])

        self.app.user_data6[0] = value_t[indx_time]
        self.label_clock.text = str(timedelta(seconds=value_t[indx_time]))

        self.app.config.set("General", "time_txt", self.app.user_data6)
        self.app.config.write()

        self.popup_timer.dismiss()

    def timer_back(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.popup_timer.dismiss()

    def btn_back_press(self, instance):
        self.sound.stop()
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.popup.dismiss()
        self.eco_mide = 0
        self.b = 0

    def start2(self):
        self.b = self.eco_mide
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(b=0, duration=self.b)

        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def on_b(self, instance, value):
        if self.pb.value <= self.eco_mide:
            self.pb.value += 1

    def setting_press(self, instance):
        dropdown = DropDown()
        for index in language:

            btn = Button(text=f"{index}", size_hint_y=None, height=20)

            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn)

        self.app = App.get_running_app()
        self.app.user_data8 = ast.literal_eval(
            self.app.config.get("General", "language")
        )

        if "lang" not in self.app.user_data8:
            self.app.user_data8["lang"] = language[1]

            self.app.config.set("General", "language", self.app.user_data8)
            self.app.config.write()

        self.mainbutton = Button(text=self.app.user_data8["lang"], height=30)

        self.mainbutton.bind(on_release=dropdown.open)

        boxdrop = BoxLayout(orientation="horizontal", size_hint_x=0.5)
        boxdrop.add_widget(Label(size_hint_x=0.25))
        boxdrop.add_widget(self.mainbutton)
        boxdrop.add_widget(Label(size_hint_x=0.25))

        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, "text", x))

        self.app = App.get_running_app()
        self.app.user_data8 = ast.literal_eval(
            self.app.config.get("General", "language")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()

        self.value_music = self.app.user_data7[1]
        self.switch_value = self.app.user_data7[0]
        main_box = BoxLayout(orientation="vertical")
        box_big = BoxLayout(orientation="vertical", size_hint=(1, 0.4), spacing=20)

        box_big.add_widget(Label(size_hint=(1, 0.2)))

        box_small = BoxLayout(orientation="horizontal", size_hint=(1, 0.2))
        box_small_two = BoxLayout(
            orientation="horizontal",
            size_hint=(1, 0.2),
        )
        box_small2 = BoxLayout(orientation="horizontal", size_hint=(1, 0.2))

        label_set = Label(
            text=f"{valume[0]}",
            font_size=font_size_all,
            color=(122 / 255, 170 / 255, 28 / 255, 1),
        )

        if get_language_now() == "image":
            x = "Мова"
        else:
            x = "Language"
        label_language = Label(
            # text="Мова",
            text=x,
            font_size=font_size_all,
            color=(122 / 255, 170 / 255, 28 / 255, 1),
        )

        self.sw = Switch(active=self.switch_value)
        box_small.add_widget(label_set)
        box_small.add_widget(self.sw)

        shadow = BoxLayout(orientation="vertical", size_hint=(1, 0.3))

        boxdrop2 = BoxLayout(orientation="horizontal", size_hint_x=0.5)

        boxdrop2.add_widget(label_language)
        boxdrop2.add_widget(Label(size_hint_x=0.01))

        box_small_two.add_widget(boxdrop2)
        box_small_two.add_widget(boxdrop)

        shadow.add_widget(box_small_two)

        box_big.add_widget(box_small)
        box_big.add_widget(shadow)

        box_big.add_widget(Label(size_hint=(1, 0.1)))

        sl = Slider(
            value_track=True,
            value_track_color=[122 / 255, 170 / 255, 28 / 255, 1],
            min=0,
            max=1,
            value=self.value_music,
        )
        sl.bind(value=self.on_value)
        self.label_set2 = Label(
            text=f"{math.trunc(self.app.user_data7[1] * 100)}%",
            size_hint=(0.2, 1),
            font_size=font_size_all,
            color=(122 / 255, 170 / 255, 28 / 255, 1),
        )
        box_small2.add_widget(self.label_set2)
        box_small2.add_widget(sl)

        box_big.add_widget(
            Label(
                text=f"{valume[1]}",
                size_hint=(1, 0.6),
                font_size=font_size_all,
                color=(122 / 255, 170 / 255, 28 / 255, 1),
            )
        )
        box_big.add_widget(box_small2)

        box_big.add_widget(Label(size_hint=(1, 0.2)))

        main_box.add_widget(box_big)
        main_box.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\exit.png",
                source=f".\\{get_language_now()}\\exit.png",
                size_hint=(1, 0.1),
                on_press=self.close_window,
            )
        )
        main_box.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\add_settings.png",
                source=f".\\{get_language_now()}\\add_settings.png",
                size_hint=(1, 0.1),
                on_press=self.add_set,
            )
        )
        main_box.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\cansel.png",
                source=f".\\{get_language_now()}\\cansel.png",
                size_hint=(1, 0.1),
                on_press=self.btn_settings_back,
            )
        )
        if get_language_now() == "image":
            x = "Налаштування"
        else:
            x = "Settings"
        self.pop = Popup(
            title=x,
            content=main_box,
            padding=(10, 0),
            size_hint=(1, None),
            height=Window.size[1] - 100,
            separator_color=(122 / 255, 170 / 255, 28 / 255, 1),
            title_align="center",
            title_color=(122 / 255, 170 / 255, 28 / 255, 1),
        )

        self.pop.open()

    def btn_settings_back(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.pop.dismiss()

    def close_window(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()

        App.get_running_app().stop()

    def on_value(self, instance, value):
        if value >= 0.999:
            value = 1
        self.value_music = value
        self.label_set2.text = f"{str(math.trunc(value * 100))}%"

    def add_set(self, instance):
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        sound = SoundLoader.load(".\\music\\btn_press.mp3")
        sound.volume = self.app.user_data7[1]
        sound.play()
        self.app = App.get_running_app()
        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        self.app.user_data7[0] = self.sw.active
        self.app.user_data7[1] = self.value_music

        self.app.config.set("General", "settings_value", self.app.user_data7)
        self.app.config.write()

        self.app = App.get_running_app()
        self.app.user_data8 = ast.literal_eval(
            self.app.config.get("General", "language")
        )

        if self.app.user_data8["lang"] == self.mainbutton.text:
            self.pop.dismiss()
        else:
            self.app.user_data8["lang"] = self.mainbutton.text

            if self.app.user_data8["lang"] == "UA":
                with open(".\\language.txt", "w") as file:
                    file.write("image")
                file.close()
            else:
                with open(".\\language.txt", "w") as file:
                    file.write("imageEnglish")
                file.close()

            self.app.config.set("General", "language", self.app.user_data8)
            self.app.config.write()

            self.pop.dismiss()

            self.layout.clear_widgets()

            self.main.clear_widgets()

            set_screen("menu")
            set_screen("check_list")


class AddMyCheckList(Screen):
    height_headerfooter = 75
    indx = 0
    scroll_distance_y = 1

    indx_spinner = {}
    spinner_name = []

    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            Rectangle(
                pos=(0, 0),
                size=Window.size,
                source=".\\image\\good.jpg",
            )

            Color(0, 0, 0, 0.4)
            Rectangle(pos=(0, 0), size=Window.size)

        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=(0, Window.size[1] - 75), size=(Window.size[0], 75))
            RoundedRectangle(
                pos=(0, 0),
                size=(Window.size[0], self.height_headerfooter),
                radius=[(20.0, 20.0), (20.0, 20.0), (0.0, 0.0), (0.0, 0.0)],
            )

    def on_enter(self):
        self.indx = 0

        self.main = BoxLayout(orientation="vertical")

        header_add = BoxLayout(orientation="horizontal", size_hint=(1, None), height=75)
        self.footer_add = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=75,
            padding=(10, 10, 10, 10),
        )
        back_button = Btn(
            on_press=lambda x: set_screen("menu"),
            size_hint=(None, 1),
            source=".\\image\\back.png",
            width=50,
        )
        back_button.bind(on_press=self.scroll_save)

        header_add.add_widget(back_button)
        header_add.add_widget(Label(size_hint=(None, 1), width=10))
        img_head = BoxLayout(
            orientation="horizontal", size_hint=(0.7, 1), padding=(10, 10)
        )
        img_head.add_widget(
            Image(
                # source="F:\\python\\kivyProjects\\image\\mini_logo.png",
                source=f".\\{get_language_now()}\\image.png",
                size_hint=(1, 1),
            )
        )
        header_add.add_widget(img_head)
        header_add.add_widget(Label(size_hint=(None, 1), width=60))

        # back_my_list = Btn(source="F:\\python\\kivyProjects\\image\\menu_list.png")
        back_my_list = Btn(source=f".\\{get_language_now()}\\myCheckList.png")
        back_my_list.bind(on_press=lambda x: set_screen("check_list"))
        back_my_list.bind(on_press=self.scroll_save)

        self.footer_add.add_widget(back_my_list)

        self.main.add_widget(header_add)

        self.gr_actions = GridLayout(
            cols=1, spacing=10, padding=(5, 15), row_default_height=70, size_hint_y=None
        )
        self.gr_actions.bind(minimum_height=self.gr_actions.setter("height"))

        self.gr_actions.add_widget(
            Btn(
                # source="F:\\python\\kivyProjects\\image\\lev_all.png",
                source=f".\\{get_language_now()}\\lev_all.png",
                size_hint=(1, None),
                height=100,
            )
        )

        self.root = ScrollView(scroll_y=self.scroll_distance_y)

        self.text = "hello"

        with open(".\\language.txt", "r") as file:
            for line in file:
                language_image = str(line)

        if language_image == "image":
            self.actions = actions
            for ii in self.actions:
                if ii[0] != "легкий" and ii[0] != "сложний" and ii[0] != "про":
                    only_actions.append(ii)
        else:
            self.actions = actions_english
            for ii in self.actions:
                if ii[0] != "легкий" and ii[0] != "сложний" and ii[0] != "про":
                    only_actions.append(ii)

        for i in range(len(self.actions)):
            self.txt = self.actions[i][0]

            if self.txt != "легкий" and self.txt != "сложний" and self.txt != "про":
                mainbtn = BoxLayout(orientation="horizontal", height=50, spacing=5)
                self.tests = BoxLayout(
                    orientation="horizontal", size_hint=(0.7, 1), spacing=2
                )

                self.label = Label(
                    text=f"{self.actions[i][0]}",
                    font_size=font_size_all,
                    color=(1, 1, 1),
                    size_hint=(0.8, 1),
                    text_size=(Window.size[0] - 85, None),
                    halign="center",
                    padding=(10, 10),
                )
                spinner = self.measured(self.actions[i][1])

                user = ast.literal_eval(
                    App.get_running_app().config.get("General", "user_data3")
                )

                if self.actions.index(self.actions[i]) > self.actions.index(
                    ["легкий", 0]
                ) and self.actions.index(self.actions[i]) < self.actions.index(
                    ["сложний", 1]
                ):
                    if self.actions[i][0] in user:
                        btn2 = Btn(
                            size_hint=(None, 1),
                            source=".\\image\\ch_pl.png",
                            width=45,
                        )
                    else:
                        btn2 = Btn(
                            size_hint=(None, 1),
                            source=".\\image\\plus2.png",
                            width=45,
                        )
                    btn3 = Btn(
                        size_hint=(None, 1),
                        source=".\\image\\info.png",
                        width=45,
                    )
                elif self.actions.index(self.actions[i]) > self.actions.index(
                    ["сложний", 1]
                ) and self.actions.index(self.actions[i]) < self.actions.index(
                    ["про", 2]
                ):
                    if actions[i][0] in user:
                        btn2 = Btn(
                            size_hint=(None, 1),
                            source=".\\image\\ch_pl_yellow.png",
                            width=45,
                        )
                    else:
                        btn2 = Btn(
                            size_hint=(None, 1),
                            source=".\\image\\plus2_yello.png",
                            width=45,
                        )
                    btn3 = Btn(
                        size_hint=(None, 1),
                        source=".\\image\\info_yello.png",
                        width=45,
                    )
                else:
                    if self.actions[i][0] in user:
                        btn2 = Btn(
                            size_hint=(None, 1),
                            source=".\\image\\ch_pl_red.png",
                            width=45,
                        )
                    else:
                        btn2 = Btn(
                            size_hint=(None, 1),
                            source=".\\image\\plus2_red.png",
                            width=45,
                        )
                    btn3 = Btn(
                        size_hint=(None, 1),
                        source=".\\image\\info_red.png",
                        width=45,
                    )

                btn2.n = self.indx
                btn2.bind(on_press=self.buttonClicked)
                btn3.n = self.indx
                btn3.bind(on_press=self.buttonDescription)

                if not spinner.text == "none":
                    self.tests.add_widget(self.label)
                    self.tests.add_widget(spinner)
                else:
                    self.label.size_hint = (1, 1)
                    self.tests.add_widget(self.label)

                mainbtn.add_widget(self.tests)
                mainbtn.add_widget(btn2)
                mainbtn.add_widget(btn3)

                self.gr_actions.add_widget(mainbtn)

                self.indx += 1

            elif self.txt == "легкий":
                self.gr_actions.add_widget(
                    Btn(
                        # source="F:\\python\\kivyProjects\\image\\lev_easy.png",
                        source=f".\\{get_language_now()}\\lev_easy.png",
                        size_hint=(1, None),
                        height=150,
                    )
                )
            elif self.txt == "сложний":
                self.gr_actions.add_widget(
                    Btn(
                        # source="F:\\python\\kivyProjects\\image\\lev_advanced.png",
                        source=f".\\{get_language_now()}\\lev_advanced.png",
                        size_hint=(1, None),
                        height=200,
                    )
                )
            elif self.txt == "про":
                self.gr_actions.add_widget(
                    Btn(
                        # source="F:\\python\\kivyProjects\\image\\lev_pro.png",
                        source=f".\\{get_language_now()}\\lev_pro.png",
                        size_hint=(1, None),
                        height=200,
                    )
                )

        self.root.add_widget(self.gr_actions)
        self.main.add_widget(self.root)
        self.main.add_widget(self.footer_add)
        self.add_widget(self.main)

    def on_leave(self):
        self.gr_actions.clear_widgets()
        self.main.clear_widgets()

    def scroll_save(self, instance):
        self.scroll_distance_y = self.root.scroll_y

    def buttonDescription(self, instance):
        self.app = App.get_running_app()
        self.app.txt = ast.literal_eval(self.app.config.get("General", "txt"))
        self.app.txt["indx"] = instance.n

        self.app.config.set("General", "txt", self.app.txt)
        self.app.config.write()

        self.scroll_distance_y = self.root.scroll_y

        set_screen("description")

    def buttonClicked(self, instance):
        state = ast.literal_eval(
            App.get_running_app().config.get("General", "user_data2")
        )

        if "State" not in state or state["State"] == 0:
            if (
                instance.n >= self.actions.index(["легкий", 0])
                and instance.n < self.actions.index(["сложний", 1]) - 1
            ):
                instance.source = ".\\image\\ch_pl.png"
            elif (
                instance.n >= self.actions.index(["сложний", 1]) - 1
                and instance.n < self.actions.index(["про", 2]) - 2
            ):
                instance.source = ".\\image\\ch_pl_yellow.png"
            else:
                instance.source = ".\\image\\ch_pl_red.png"
            self.app = App.get_running_app()
            self.app.user_data = ast.literal_eval(
                self.app.config.get("General", "user_data")
            )

            self.app.user_data[only_actions[instance.n][0]] = self.indx_spinner[
                self.spinner_name[instance.n]
            ]

            self.app = App.get_running_app()
            self.app.user_data3 = ast.literal_eval(
                self.app.config.get("General", "user_data3")
            )
            self.app.config.set("General", "user_data", self.app.user_data)
            self.app.config.write()

            if self.app.user_data3.count(only_actions[instance.n][0]) == 0:
                self.app.user_data3.append(only_actions[instance.n][0])

                self.app.config.set("General", "user_data3", self.app.user_data3)
                self.app.config.write()

                self.app = App.get_running_app()
                self.app.user_data7 = ast.literal_eval(
                    self.app.config.get("General", "settings_value")
                )

                sound = SoundLoader.load(".\\music\\btn_press.mp3")
                sound.volume = self.app.user_data7[1]

                sound.play()

    def measured(self, i):
        if i == "Ват.":
            self.spin = Spinner(
                text=f"{wat[0]}",
                values=wat,
                size_hint=(0.2, 1),
                background_color=(1, 1, 1, 0),
            )
        elif i == "л.":
            self.spin = Spinner(
                text=f"{lit[0]}",
                values=lit,
                size_hint=(0.2, 1),
                background_color=(1, 1, 1, 0),
            )
        elif i == "кг.":
            self.spin = Spinner(
                text=f"{kg[0]}",
                values=kg,
                size_hint=(0.2, 1),
                background_color=(1, 1, 1, 0),
            )
        else:
            self.spin2 = Spinner(
                text="none",
                values=("none"),
                size_hint=(0.2, 1),
                background_color=(1, 1, 1, 0),
            )
            self.indx_spinner[self.spin2] = self.spin2.text
            self.spinner_name.append(self.spin2)
            return self.spin2

        self.spin.bind(text=self.show_selected_value)

        self.indx_spinner[self.spin] = self.spin.text

        self.spinner_name.append(self.spin)

        return self.spin

    def show_selected_value(self, spinner, text):
        self.indx_spinner[spinner] = text


class Description(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            Rectangle(
                pos=(0, 0),
                size=Window.size,
                source=".\\image\\good.jpg",
            )

            Color(0, 0, 0, 0.4)
            Rectangle(pos=(0, 0), size=Window.size)

        with self.canvas:
            Color(0, 0, 0, 1)

            Rectangle(pos=(0, Window.size[1] - 75), size=(Window.size[0], 75))

    def on_enter(self):
        self.main = BoxLayout(orientation="vertical")

        header_add = BoxLayout(orientation="horizontal", size_hint=(1, None), height=75)
        back_button = Btn(
            on_press=lambda x: set_screen("add_check_list"),
            size_hint=(None, 1),
            source=".\\image\\back.png",
            width=50,
        )

        header_add.add_widget(back_button)
        header_add.add_widget(Label(size_hint=(None, 1), width=10))
        img_head = BoxLayout(
            orientation="horizontal", size_hint=(0.7, 1), padding=(10, 10)
        )
        img_head.add_widget(
            Image(
                # source="F:\\python\\kivyProjects\\image\\mini_logo.png",
                source=f".\\{get_language_now()}\\image.png",
                size_hint=(1, 1),
            )
        )
        header_add.add_widget(img_head)
        header_add.add_widget(Label(size_hint=(None, 1), width=60))

        self.main.add_widget(header_add)

        self.app = App.get_running_app()
        self.app.txt = ast.literal_eval(self.app.config.get("General", "txt"))

        indx_file = self.app.txt["indx"]

        file_with_description = []

        with open(".\\language.txt", "r") as file:
            for line in file:
                language_image = str(line)

        if language_image == "image":
            with open("check_description.txt", "r") as file:
                for line in file:
                    file_with_description.append(line)
        else:
            with open("check_description_english.txt", "r") as file:
                for line in file:
                    file_with_description.append(line)

        self.root = ScrollView()
        self.root.add_widget(
            Label(
                text=file_with_description[indx_file],
                text_size=(Window.size[0] - 40, None),
                font_size=font_size_all,
                color=(1, 1, 1),
            )
        )

        self.main.add_widget(self.root)

        self.add_widget(self.main)

    def on_leave(self):
        self.root.clear_widgets()
        self.main.clear_widgets()


class Btn(ButtonBehavior, Image):
    n = NumericProperty(0)


class Btn_remove(ButtonBehavior, Image):
    n_remove = NumericProperty(0)


class MyButton_check(ButtonBehavior, Image):
    state_checkbox = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = ".\\image\\checkbox_no.png"


def eco_mide_procent(mide):
    eco_mide += mide


def get_language_now():
    i = "imageEnglish"
    app = App.get_running_app()
    app.user_data8 = ast.literal_eval(app.config.get("General", "language"))
    if "lang" not in app.user_data8:
        app.user_data8["lang"] = language[1]
    elif app.user_data8["lang"] == "UA":
        i = "image"
    else:
        i = "imageEnglish"
    return i


def set_screen(name_screen):
    app = App.get_running_app()
    app.user_data7 = ast.literal_eval(app.config.get("General", "settings_value"))

    soundr = SoundLoader.load(".\\music\\btn_press.mp3")
    soundr.volume = app.user_data7[1]
    soundr.play()
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(MyCheckList(name="check_list"))
sm.add_widget(AddMyCheckList(name="add_check_list"))
sm.add_widget(Description(name="description"))


class CheckListApp(App):

    def __init__(self, **kvargs):
        super().__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection("General")
        config.setdefault("General", "user_data", "{}")
        config.setdefault("General", "user_data2", "{}")
        config.setdefault("General", "user_data3", "[]")
        config.setdefault("General", "user_data4", "[]")
        config.setdefault("General", "txt", "{}")
        config.setdefault("General", "time_txt", [value_t[0]])
        config.setdefault("General", "settings_value", [True, 0.3])
        config.setdefault("General", "language", "{}")

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, "%(appname)s.ini"))
        self.user_data = ast.literal_eval(self.config.get("General", "user_data"))

        self.user_data2 = ast.literal_eval(self.config.get("General", "user_data2"))

        self.user_data3 = ast.literal_eval(self.config.get("General", "user_data3"))

        self.user_data4 = ast.literal_eval(self.config.get("General", "user_data4"))

        self.user_data5 = ast.literal_eval(self.config.get("General", "txt"))

        self.user_data6 = ast.literal_eval(self.config.get("General", "time_txt"))

        self.user_data7 = ast.literal_eval(self.config.get("General", "settings_value"))

        self.user_data8 = ast.literal_eval(self.config.get("General", "language"))

    def get_application_config(self):
        return super().get_application_config(
            "{}/%(appname)s.ini".format(self.directory)
        )

    def build(self):
        self.sound_all = SoundLoader.load(".\\music\\landscape.mp3")
        self.sound_all.loop = True
        self.sound_all.volume = 0.2

        app = App.get_running_app()

        app.user_data7 = ast.literal_eval(app.config.get("General", "settings_value"))
        self.no_again = app.user_data7[0]
        Clock.schedule_interval(self.music, 0.1)

        return sm

    def music(self, dt):
        self.app = App.get_running_app()

        self.app.user_data7 = ast.literal_eval(
            self.app.config.get("General", "settings_value")
        )

        if self.app.user_data7[0] == False and self.no_again == False:
            self.sound_all.play()
            self.sound_all.stop()
            self.no_again = True

        if self.no_again == True:
            if self.app.user_data7[0]:
                self.sound_all.play()
                self.no_again = False


if __name__ == "__main__":
    CheckListApp().run()
