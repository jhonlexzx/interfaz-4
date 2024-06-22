import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

class Equipo {
    private String nombre;
    private String entrenador;

    public Equipo(String nombre, String entrenador) {
        this.nombre = nombre;
        this.entrenador = entrenador;
    }

    public String getNombre() {
        return nombre;
    }

    @Override
    public String toString() {
        return nombre;
    }
}

class Partido {
    private Equipo equipoLocal;
    private Equipo equipoVisitante;
    private String resultado;

    public Partido(Equipo equipoLocal, Equipo equipoVisitante, String resultado) {
        this.equipoLocal = equipoLocal;
        this.equipoVisitante = equipoVisitante;
        this.resultado = resultado;
    }

    @Override
    public String toString() {
        return equipoLocal.getNombre() + " vs " + equipoVisitante.getNombre() + " - " + resultado;
    }
}

class Grupo {
    private String nombre;
    private ArrayList<Equipo> equipos;

    public Grupo(String nombre) {
        this.nombre = nombre;
        this.equipos = new ArrayList<>();
    }

    public void agregarEquipo(Equipo equipo) {
        equipos.add(equipo);
    }

    @Override
    public String toString() {
        return nombre;
    }

    public ArrayList<Equipo> getEquipos() {
        return equipos;
    }
}

class Estadio {
    private String nombre;
    private String ciudad;
    private int capacidad;

    public Estadio(String nombre, String ciudad, int capacidad) {
        this.nombre = nombre;
        this.ciudad = ciudad;
        this.capacidad = capacidad;
    }

    @Override
    public String toString() {
        return nombre + " - " + ciudad + " - " + capacidad;
    }
}

class Mundial {
    private ArrayList<Grupo> grupos;
    private ArrayList<Estadio> estadios;
    private ArrayList<Partido> partidos;

    public Mundial() {
        this.grupos = new ArrayList<>();
        this.estadios = new ArrayList<>();
        this.partidos = new ArrayList<>();
    }

    public void registrarGrupo(Grupo grupo) {
        grupos.add(grupo);
    }

    public void registrarEstadio(Estadio estadio) {
        estadios.add(estadio);
    }

    public void registrarPartido(Partido partido) {
        partidos.add(partido);
    }

    public ArrayList<Grupo> getGrupos() {
        return grupos;
    }

    public ArrayList<Estadio> getEstadios() {
        return estadios;
    }

    public ArrayList<Partido> getPartidos() {
        return partidos;
    }
}

public class MundialApp extends JFrame {
    private Mundial mundial;
    private JTabbedPane tabbedPane;
    private DefaultListModel<Equipo> equipoListModel;
    private DefaultListModel<Partido> partidoListModel;
    private DefaultListModel<Grupo> grupoListModel;
    private DefaultListModel<Estadio> estadioListModel;
    private JComboBox<Equipo> comboEquipoLocal;
    private JComboBox<Equipo> comboEquipoVisitante;

    public MundialApp() {
        mundial = new Mundial();
        equipoListModel = new DefaultListModel<>();
        partidoListModel = new DefaultListModel<>();
        grupoListModel = new DefaultListModel<>();
        estadioListModel = new DefaultListModel<>();

        setTitle("Gestión del Mundial");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        tabbedPane = new JTabbedPane();

        initTabEquipos();
        initTabPartidos();
        initTabGrupos();
        initTabEstadios();

        add(tabbedPane);
    }

    private void initTabEquipos() {
        JPanel panel = new JPanel(new BorderLayout());
        tabbedPane.addTab("Equipos", panel);

        JPanel form = new JPanel(new GridLayout(3, 2));
        panel.add(form, BorderLayout.NORTH);

        JTextField entryNombreEquipo = new JTextField();
        JTextField entryEntrenadorEquipo = new JTextField();

        form.add(new JLabel("Nombre:"));
        form.add(entryNombreEquipo);
        form.add(new JLabel("Entrenador:"));
        form.add(entryEntrenadorEquipo);

        JButton btnRegistrarEquipo = new JButton("Registrar Equipo");
        form.add(btnRegistrarEquipo);

        JList<Equipo> listaEquipos = new JList<>(equipoListModel);
        panel.add(new JScrollPane(listaEquipos), BorderLayout.CENTER);

        btnRegistrarEquipo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nombre = entryNombreEquipo.getText();
                String entrenador = entryEntrenadorEquipo.getText();
                if (!nombre.isEmpty() && !entrenador.isEmpty()) {
                    Equipo equipo = new Equipo(nombre, entrenador);
                    if (!mundial.getGrupos().isEmpty()) {
                        mundial.getGrupos().get(0).agregarEquipo(equipo);
                        equipoListModel.addElement(equipo);
                        comboEquipoLocal.addItem(equipo);
                        comboEquipoVisitante.addItem(equipo);
                    }
                    entryNombreEquipo.setText("");
                    entryEntrenadorEquipo.setText("");
                }
            }
        });
    }

    private void initTabPartidos() {
        JPanel panel = new JPanel(new BorderLayout());
        tabbedPane.addTab("Partidos", panel);

        JPanel form = new JPanel(new GridLayout(4, 2));
        panel.add(form, BorderLayout.NORTH);

        comboEquipoLocal = new JComboBox<>();
        comboEquipoVisitante = new JComboBox<>();
        JTextField entryResultadoPartido = new JTextField();

        form.add(new JLabel("Equipo Local:"));
        form.add(comboEquipoLocal);
        form.add(new JLabel("Equipo Visitante:"));
        form.add(comboEquipoVisitante);
        form.add(new JLabel("Resultado:"));
        form.add(entryResultadoPartido);

        JButton btnRegistrarPartido = new JButton("Registrar Partido");
        form.add(btnRegistrarPartido);

        JList<Partido> listaPartidos = new JList<>(partidoListModel);
        panel.add(new JScrollPane(listaPartidos), BorderLayout.CENTER);

        btnRegistrarPartido.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Equipo equipoLocal = (Equipo) comboEquipoLocal.getSelectedItem();
                Equipo equipoVisitante = (Equipo) comboEquipoVisitante.getSelectedItem();
                String resultado = entryResultadoPartido.getText();
                if (equipoLocal != null && equipoVisitante != null && !resultado.isEmpty()) {
                    Partido partido = new Partido(equipoLocal, equipoVisitante, resultado);
                    mundial.registrarPartido(partido);
                    partidoListModel.addElement(partido);
                    entryResultadoPartido.setText("");
                }
            }
        });
    }

    private void initTabGrupos() {
        JPanel panel = new JPanel(new BorderLayout());
        tabbedPane.addTab("Grupos", panel);

        JPanel form = new JPanel(new GridLayout(2, 2));
        panel.add(form, BorderLayout.NORTH);

        JTextField entryNombreGrupo = new JTextField();

        form.add(new JLabel("Nombre:"));
        form.add(entryNombreGrupo);

        JButton btnRegistrarGrupo = new JButton("Registrar Grupo");
        form.add(btnRegistrarGrupo);

        JList<Grupo> listaGrupos = new JList<>(grupoListModel);
        panel.add(new JScrollPane(listaGrupos), BorderLayout.CENTER);

        btnRegistrarGrupo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nombre = entryNombreGrupo.getText();
                if (!nombre.isEmpty()) {
                    Grupo grupo = new Grupo(nombre);
                    mundial.registrarGrupo(grupo);
                    grupoListModel.addElement(grupo);
                    entryNombreGrupo.setText("");
                }
            }
        });
    }

    private void initTabEstadios() {
        JPanel panel = new JPanel(new BorderLayout());
        tabbedPane.addTab("Estadios", panel);

        JPanel form = new JPanel(new GridLayout(4, 2));
        panel.add(form, BorderLayout.NORTH);

        JTextField entryNombreEstadio = new JTextField();
        JTextField entryCiudadEstadio = new JTextField();
        JTextField entryCapacidadEstadio = new JTextField();

        form.add(new JLabel("Nombre:"));
        form.add(entryNombreEstadio);
        form.add(new JLabel("Ciudad:"));
        form.add(entryCiudadEstadio);
        form.add(new JLabel("Capacidad:"));
        form.add(entryCapacidadEstadio);

        JButton btnRegistrarEstadio = new JButton("Registrar Estadio");
        form.add(btnRegistrarEstadio);

        JList<Estadio> listaEstadios = new JList<>(estadioListModel);
        panel.add(new JScrollPane(listaEstadios), BorderLayout.CENTER);

        btnRegistrarEstadio.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nombre = entryNombreEstadio.getText();
                String ciudad = entryCiudadEstadio.getText();
                String capacidadStr = entryCapacidadEstadio.getText();
                if (!nombre.isEmpty() && !ciudad.isEmpty() && !capacidadStr.isEmpty()) {
                    try {
                        int capacidad = Integer.parseInt(capacidadStr);
                        Estadio estadio = new Estadio(nombre, ciudad, capacidad);
                        mundial.registrarEstadio(estadio);
                        estadioListModel.addElement(estadio);
                        entryNombreEstadio.setText("");
                        entryCiudadEstadio.setText("");
                        entryCapacidadEstadio.setText("");
                    } catch (NumberFormatException ex) {
                        JOptionPane.showMessageDialog(MundialApp.this, "Capacidad debe ser un número entero.");
                    }
                }
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new MundialApp().setVisible(true);
            }
        });
    }
}
