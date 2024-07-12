import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gio, Gtk
# Falta agregar más cosas
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self.get_application()
        self.set_default_size(1920, 1080)
        # Header Bar
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Simulación")
        # Menu Button
        menu_button_model = Gio.Menu()
        menu_button_model.append("About", "app.about")
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)
        # Ventana
        self.scroll = Gtk.ScrolledWindow()
        self.main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        self.data_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        self.set_child(self.scroll)
        self.scroll.set_child(self.main_box)
        self.main_box.append(self.data_box)
        # Titulo1
        self.make_label_title("Parametros SIR")
        # Entry1
        self.entry_infeccion_probable = self.make_entry("Tasa de transmisión [B]", "")
        # Entry2
        self.entry_promedio_pasos = self.make_entry("Tasa de transmisión/Promedio pasos [Y]", "")
        # Entry3
        self.entry_num_ciudadanos = self.make_entry("Población total (ciudadanos) [N]", "")
        # Titulo2
        self.make_label_title("Comunidad")
        # Entry4
        self.entry_probabilidad_coneccion_fisica = self.make_entry("Probabilidad de darse una conección estrecha", "")
        # Entry5
        self.entry_promedio_coneccion_fisica = self.make_entry("Promedio conección física", "")
        # Entry5
        self.entry_num_infectados = self.make_entry("Población de infectados iniciales", "")
        # Titulo3
        self.make_label_title("Simulación")
        # Entry6
        self.entry_dias_simulacion = self.make_entry("Días", "")
        # Titulo4
        self.make_label_title("Enfermedad")
        # Entry7
        self.entry_infeccion_estrecho = self.make_entry("Tasa de transmisión para un contacto estrecho", "")
        # Titulo5
        self.make_label_title("Colores")
        # Labels
        self.make_label("Población susceptible<span foreground='blue'><big> ◉ </big></span>Azul")
        self.make_label("Poblacion infectada<span foreground='yellow'><big> ◉ </big></span>Amarillo")
        self.make_label("Poblacion recuperada<span foreground='red'><big> ◉ </big></span>Rojo")
        # Button
        self.start_button = Gtk.Button.new_with_label("Comenzar Simulación")
        self.start_button.connect("clicked", self.on_start_button_clicked)
        self.data_box.append(self.start_button)

    def make_label_title(self, texto):
        label = Gtk.Label()
        label.set_markup(f"<span foreground='purple'><big><i><b>{texto}</b></i></big></span>")
        label.set_margin_start(15)
        label.set_halign(1)
        label.set_hexpand(True)
        self.data_box.append(label)

    def make_label(self, texto):
        label = Gtk.Label()
        label.set_markup(f"<i><b>{texto}</b></i>")
        label.set_margin_start(30)
        label.set_halign(1)
        label.set_hexpand(True)
        self.data_box.append(label)

    def make_entry(self, texto, inicial):
        entry = Gtk.Entry()
        entry.set_text(inicial)
        entry.set_margin_end(10)
        box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10)
        label = Gtk.Label.new(texto)
        label.set_margin_start(30)
        label.set_halign(1)
        label.set_hexpand(True)
        box.append(label)
        box.append(entry)
        self.data_box.append(box)
        return entry    

    def on_start_button_clicked(self, button):
        print("Ta funcionando")

class MyApp(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.example.GtkApplication", **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = MainWindow(application=self)
        self.window.present()

app = MyApp()
app.run(None)
