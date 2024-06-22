import tkinter as tk
from tkinter import ttk
import time  # Para simular la animación

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def mostrar_info(self):
        jugadores_info = "\n".join([jugador.mostrar_info() for jugador in self.jugadores])
        return f"Equipo: {self.nombre}\nEntrenador: {self.entrenador}\nJugadores:\n{jugadores_info}"

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"{self.nombre} - {self.edad} años - {self.posicion}"

class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.resultado = None

    def jugar_partido(self, resultado):
        self.resultado = resultado

    def mostrar_resultado(self):
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre} - Resultado: {self.resultado}"

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def mostrar_info(self):
        equipos_info = "\n".join([equipo.mostrar_info() for equipo in self.equipos])
        return f"Grupo: {self.nombre}\nEquipos:\n{equipos_info}"

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.nombre} - Ciudad: {self.ciudad} - Capacidad: {self.capacidad}"

class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def generar_fixture(self):
        # Lógica para generar el fixture del mundial
        pass

class MundialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mundial App")

        # Ajustar tamaño de la ventana y centrar en la pantalla
        self.root.geometry("1000x600")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (1000 // 2)
        y = (screen_height // 2) - (600 // 2)
        self.root.geometry(f"1000x600+{x}+{y}")

        # Crear una instancia de Mundial
        self.mundial = Mundial()

        # Estilo para los widgets
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("TEntry", fieldbackground="#ffffff")
        self.style.configure("TButton", background="#e0e0e0", font=("Arial", 10))
        self.style.configure("TNotebook", background="#f0f0f0")
        self.style.configure("TNotebook.Tab", background="#c0c0c0", font=("Arial", 10))

        # Notebook para las pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear las pestañas
        self.tab_equipos = ttk.Frame(self.notebook)
        self.tab_partidos = ttk.Frame(self.notebook)
        self.tab_grupos = ttk.Frame(self.notebook)
        self.tab_estadios = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_equipos, text="Equipos")
        self.notebook.add(self.tab_partidos, text="Partidos")
        self.notebook.add(self.tab_grupos, text="Grupos")
        self.notebook.add(self.tab_estadios, text="Estadios")

        # Inicializar contenido de las pestañas
        self.init_tab_equipos()
        self.init_tab_partidos()
        self.init_tab_grupos()
        self.init_tab_estadios()

    def init_tab_equipos(self):
        # Frame para el registro de equipos
        self.frame_registro_equipo = ttk.LabelFrame(self.tab_equipos, text="Registrar Equipo", style="TFrame")
        self.frame_registro_equipo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.frame_registro_equipo, text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre_equipo = ttk.Entry(self.frame_registro_equipo)
        self.entry_nombre_equipo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_registro_equipo, text="Entrenador").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_entrenador_equipo = ttk.Entry(self.frame_registro_equipo)
        self.entry_entrenador_equipo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.frame_registro_equipo, text="Registrar Equipo", command=self.registrar_equipo).grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        # Lista para mostrar los equipos
        self.lista_equipos = tk.Listbox(self.frame_registro_equipo, height=10)
        self.lista_equipos.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Frame para el registro de jugadores
        self.frame_registro_jugador = ttk.LabelFrame(self.tab_equipos, text="Registrar Jugador", style="TFrame")
        self.frame_registro_jugador.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.frame_registro_jugador, text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre_jugador = ttk.Entry(self.frame_registro_jugador)
        self.entry_nombre_jugador.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_registro_jugador, text="Edad").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_edad_jugador = ttk.Entry(self.frame_registro_jugador)
        self.entry_edad_jugador.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_registro_jugador, text="Posición").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_posicion_jugador = ttk.Entry(self.frame_registro_jugador)
        self.entry_posicion_jugador.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.frame_registro_jugador, text="Registrar Jugador", command=self.registrar_jugador).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # Expandir los frames secundarios proporcionalmente
        self.tab_equipos.columnconfigure(0, weight=1)
        self.tab_equipos.columnconfigure(1, weight=1)
        self.tab_equipos.rowconfigure(0, weight=1)

    def init_tab_partidos(self):
        # Frame para gestionar partidos
        self.frame_gestion_partido = ttk.LabelFrame(self.tab_partidos, text="Gestionar Partido", style="TFrame")
        self.frame_gestion_partido.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.frame_gestion_partido, text="Equipo Local").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_equipo_local = ttk.Combobox(self.frame_gestion_partido, state="readonly")
        self.combo_equipo_local.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_gestion_partido, text="Equipo Visitante").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_equipo_visitante = ttk.Combobox(self.frame_gestion_partido, state="readonly")
        self.combo_equipo_visitante.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_gestion_partido, text="Resultado").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_resultado_partido = ttk.Entry(self.frame_gestion_partido)
        self.entry_resultado_partido.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.frame_gestion_partido, text="Registrar Partido", command=self.registrar_partido).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # Lista para mostrar los partidos
        self.lista_partidos = tk.Listbox(self.frame_gestion_partido, height=10)
        self.lista_partidos.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Expandir los frames secundarios proporcionalmente
        self.tab_partidos.columnconfigure(0, weight=1)
        self.tab_partidos.rowconfigure(0, weight=1)

    def init_tab_grupos(self):
        # Frame para registrar y mostrar grupos
        self.frame_registro_grupo = ttk.LabelFrame(self.tab_grupos, text="Registrar Grupo", style="TFrame")
        self.frame_registro_grupo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.frame_registro_grupo, text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre_grupo = ttk.Entry(self.frame_registro_grupo)
        self.entry_nombre_grupo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.frame_registro_grupo, text="Registrar Grupo", command=self.registrar_grupo).grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        # Lista para mostrar los grupos
        self.lista_grupos = tk.Listbox(self.frame_registro_grupo, height=10)
        self.lista_grupos.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Expandir los frames secundarios proporcionalmente
        self.tab_grupos.columnconfigure(0, weight=1)
        self.tab_grupos.rowconfigure(0, weight=1)

    def init_tab_estadios(self):
        # Frame para registrar y mostrar estadios
        self.frame_registro_estadio = ttk.LabelFrame(self.tab_estadios, text="Registrar Estadio", style="TFrame")
        self.frame_registro_estadio.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.frame_registro_estadio, text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre_estadio = ttk.Entry(self.frame_registro_estadio)
        self.entry_nombre_estadio.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_registro_estadio, text="Ciudad").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_ciudad_estadio = ttk.Entry(self.frame_registro_estadio)
        self.entry_ciudad_estadio.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_registro_estadio, text="Capacidad").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_capacidad_estadio = ttk.Entry(self.frame_registro_estadio)
        self.entry_capacidad_estadio.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.frame_registro_estadio, text="Registrar Estadio", command=self.registrar_estadio).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # Lista para mostrar los estadios
        self.lista_estadios = tk.Listbox(self.frame_registro_estadio, height=10)
        self.lista_estadios.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Expandir los frames secundarios proporcionalmente
        self.tab_estadios.columnconfigure(0, weight=1)
        self.tab_estadios.rowconfigure(0, weight=1)

    def registrar_equipo(self):
        nombre = self.entry_nombre_equipo.get()
        entrenador = self.entry_entrenador_equipo.get()
        if nombre and entrenador:
            equipo = Equipo(nombre, entrenador)
            self.mundial.grupos[0].agregar_equipo(equipo)  # Asumimos que el grupo ya existe
            self.lista_equipos.insert(tk.END, equipo.nombre)
            self.entry_nombre_equipo.delete(0, tk.END)
            self.entry_entrenador_equipo.delete(0, tk.END)

    def registrar_jugador(self):
        nombre = self.entry_nombre_jugador.get()
        edad = self.entry_edad_jugador.get()
        posicion = self.entry_posicion_jugador.get()
        if nombre and edad and posicion:
            jugador = Jugador(nombre, edad, posicion)
            equipo_index = self.lista_equipos.curselection()[0]
            equipo = self.mundial.grupos[0].equipos[equipo_index]  # Asumimos que el grupo ya existe
            equipo.agregar_jugador(jugador)
            self.entry_nombre_jugador.delete(0, tk.END)
            self.entry_edad_jugador.delete(0, tk.END)
            self.entry_posicion_jugador.delete(0, tk.END)

    def registrar_partido(self):
        equipo_local = self.combo_equipo_local.get()
        equipo_visitante = self.combo_equipo_visitante.get()
        resultado = self.entry_resultado_partido.get()
        if equipo_local and equipo_visitante and resultado:
            equipo_local = next(e for e in self.mundial.grupos[0].equipos if e.nombre == equipo_local)
            equipo_visitante = next(e for e in self.mundial.grupos[0].equipos if e.nombre == equipo_visitante)
            partido = Partido(equipo_local, equipo_visitante)
            partido.jugar_partido(resultado)
            self.lista_partidos.insert(tk.END, partido.mostrar_resultado())
            self.entry_resultado_partido.delete(0, tk.END)

    def registrar_grupo(self):
        nombre = self.entry_nombre_grupo.get()
        if nombre:
            grupo = Grupo(nombre)
            self.mundial.registrar_grupo(grupo)
            self.lista_grupos.insert(tk.END, grupo.nombre)
            self.entry_nombre_grupo.delete(0, tk.END)

    def registrar_estadio(self):
        nombre = self.entry_nombre_estadio.get()
        ciudad = self.entry_ciudad_estadio.get()
        capacidad = self.entry_capacidad_estadio.get()
        if nombre and ciudad and capacidad:
            estadio = Estadio(nombre, ciudad, capacidad)
            self.mundial.registrar_estadio(estadio)
            self.lista_estadios.insert(tk.END, estadio.mostrar_info())
            self.entry_nombre_estadio.delete(0, tk.END)
            self.entry_ciudad_estadio.delete(0, tk.END)
            self.entry_capacidad_estadio.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MundialApp(root)
    root.mainloop()
