import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gio, Gtk
from simulador import Simulador
from enfermedad import Enfermedad
from comunidad import Comunidad
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self.get_application()
        self.set_default_size(1200, 800)
        self.connect("destroy", self.on_destroy)
        self.entries = {}
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
        self.entry_infeccion_probable = self.make_entry("Tasa de transmisión [B]", "0.3", "trasmision")
        # Entry2
        self.entry_promedio_pasos = self.make_entry("Tasa de transmisión/Promedio pasos [Y]", "18", "pasos")
        # Entry3
        self.entry_num_ciudadanos = self.make_entry("Población total (ciudadanos) [N]", "20000", "poblacion")
        # Titulo2
        self.make_label_title("Comunidad")
        # Entry4
        self.entry_probabilidad_coneccion_fisica = self.make_entry("Probabilidad de darse una conección estrecha", "0.8", "estrecho")
        # Entry5
        self.entry_promedio_coneccion_fisica = self.make_entry("Promedio conección física", "8", "fisica")
        # Entry5
        self.entry_num_infectados = self.make_entry("Población de infectados iniciales", "10", "infectados")
        # Titulo3
        self.make_label_title("Simulación")
        # Entry6
        self.entry_dias_simulacion = self.make_entry("Días", "60", "duracion")
        # Titulo4
        self.make_label_title("Familias")
        # Entry7
        self.entry_infeccion_estrecho = self.make_entry("Cantidad de familias", "200", "familias")
        # Titulo5
        self.make_label_title("Colores")
        # Labels
        self.make_label("Población susceptible<span foreground='green'><big> ◉ </big></span>Verde")
        self.make_label("Poblacion infectada<span foreground='red'><big> ◉ </big></span>Rojo")
        self.make_label("Poblacion recuperada<span foreground='blue'><big> ◉ </big></span>Azul")
        # Button
        self.start_button = Gtk.Button.new_with_label("Comenzar Simulación")
        self.start_button.connect("clicked", self.on_start_button_clicked)
        self.data_box.append(self.start_button)
        self.imagen_resultado = Gtk.Picture()
        self.data_box.append(self.imagen_resultado)

    def load_figure(self):
        self.imagen_resultado.set_filename("./Resultado_Simulacion.png")

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

    def make_entry(self, texto, inicial, id_entry):
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
        self.entries[id_entry] = entry
        self.data_box.append(box)
        return entry

    def on_start_button_clicked(self, button):
        tasa_trasmision = self.entries["trasmision"].get_buffer().get_text()
        prom_pasos = self.entries["pasos"].get_buffer().get_text()
        poblacion = self.entries["poblacion"].get_buffer().get_text()
        estrecho = self.entries["estrecho"].get_buffer().get_text()
        con_fisica = self.entries["fisica"].get_buffer().get_text()
        infectados = self.entries["infectados"].get_buffer().get_text()
        duracion = self.entries["duracion"].get_buffer().get_text()
        familias = self.entries["familias"].get_buffer().get_text()

        try:
            tasa_trasmision = float(tasa_trasmision)
            prom_pasos = int(prom_pasos)
            poblacion = int(poblacion)
            estrecho = float(estrecho)
            con_fisica = float(con_fisica)
            infectados = int(infectados)
            duracion = int(duracion)
            familias = int(familias)
            print("Iniciando simulación")
            sim = Simulador()
            virus = Enfermedad(infeccion_probable=tasa_trasmision,
                               promedio_pasos=prom_pasos)
            talca = Comunidad(num_ciudadanos=poblacion,
                              promedio_conexion_fisica=con_fisica,
                              enfermedad=virus,
                              num_infectados=infectados,
                              num_familias=familias,
                              probabilidad_conexion_fisica=estrecho)
            sim.set_comunidad(talca)
            sim.inicializar_comunidad()
            sim.simular(duracion)
            self.crear_grafico()

        except ValueError:
            print("Los datos ingresados son incorrectos")

    def crear_grafico(self):
        resultado = pd.read_csv("./reporte_simulacion.csv")
        resultado.drop("Dia", axis=1, inplace=True)
        colores = ListedColormap(["green", "red", "blue"])
        resultado.plot(title="Resultado de la simulación", xlabel="Dias",
                       ylabel="Cantidad", colormap=colores, lw=3,
                       figsize=(10,10))
        plt.savefig("Resultado_Simulacion.png")

    def on_destroy(self, window):
        self.close()


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
