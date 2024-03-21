from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QTabWidget, QTextBrowser, QMessageBox, QFileDialog
from simbolos import TablaSimbolos
from funciones import *
import gramatica as g

# ---------------------------------------------------------------------------- #
#                              VARIABLES GLOBALES                              #
# ---------------------------------------------------------------------------- #
errores = []
resultados = []

class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('OLC Script')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #D6E4F0;")

        # Barra de navegación
        menubar = self.menuBar()

        archivo_menu = menubar.addMenu('Archivo')
        archivo_menu.addAction('Crear', self.crearArchivo).setStatusTip(
            'Crear un nuevo archivo')
        archivo_menu.addAction('Abrir', self.abrirArchivo).setStatusTip(
            'Abrir un archivo existente')
        archivo_menu.addAction('Guardar', self.guardarArchivo).setStatusTip(
            'Guardar el archivo actual')

        # Recuadro para escribir
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 30, 400, 400)
        self.text_edit.setStyleSheet(
            "background-color: #072541; color: #ffffff; font-family: Arial; font-size: 12pt;")

        # Botones Ejecutar, Mostrar reportes, Limpiar editor
        ejecutar_btn = QPushButton('Ejecutar', self)
        ejecutar_btn.setGeometry(10, 440, 100, 30)
        ejecutar_btn.setStyleSheet(
            "background-color: #42855B; color: #ffffff;")
        ejecutar_btn.clicked.connect(self.Ejecutar)

        reportes_btn = QPushButton('Mostrar Reportes', self)
        reportes_btn.setGeometry(120, 440, 150, 30)
        reportes_btn.setStyleSheet(
            "background-color: #22092C; color: #ffffff;")
        reportes_btn.clicked.connect(self.mostrarReportes)
        
        limpiar_btn = QPushButton('Limpiar consola', self)
        limpiar_btn.setGeometry(280, 440, 100, 30)
        limpiar_btn.setStyleSheet(
            "background-color: #496989; color: #ffffff;")
        limpiar_btn.clicked.connect(self.Limpiar)

        # Recuadro de pestañas (Consola, Tabla de símbolos, Errores)
        tab_widget = QTabWidget(self)
        tab_widget.setGeometry(430, 30, 350, 400)
        tab_widget.setStyleSheet(
            "QTabBar::tab:selected { background-color: #519872; } QTabBar::tab:!selected { background-color: #A4B494; }")

        self.consola_tab = QTextBrowser()
        tab_widget.addTab(self.consola_tab, 'Consola')
        self.consola_tab.setStyleSheet(
            "background-color: #000000; color: #ffffff; font-family: Arial; font-size: 12pt;")
        self.consola_tab.setFixedSize(348, 375)

        self.tabla_simbolos_tab = QTextBrowser()
        tab_widget.addTab(self.tabla_simbolos_tab, 'Tabla de Símbolos')
        self.tabla_simbolos_tab.setStyleSheet(
            "background-color: #000000; color: #ffffff; font-family: Arial; font-size: 12pt;")
        self.tabla_simbolos_tab.setFixedSize(348, 375)

        self.errores_tab = QTextBrowser()
        tab_widget.addTab(self.errores_tab, 'Errores')
        self.errores_tab.setStyleSheet(
            "background-color: #000000; color: #ffffff; font-family: Arial; font-size: 12pt;")
        self.errores_tab.setFixedSize(348, 375)

        self.show()

    def crearArchivo(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Guardar Archivo", "", "OLC Files (*.olc)")
        if filename:
            if not filename.endswith('.olc'):
                filename += '.olc'
            with open(filename, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def abrirArchivo(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Abrir Archivo", "", "OLC Files (*.olc)")
        if filename:
            with open(filename, 'r') as file:
                self.text_edit.setPlainText(file.read())

    def guardarArchivo(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Guardar Archivo", "", "OLC Files (*.olc)")
        if filename:
            with open(filename, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def Ejecutar(self):
        ts = TablaSimbolos()
        instrucciones = g.parse(self.text_edit.toPlainText())
        self.consola_tab.clear()
        self.errores_tab.clear()
        self.tabla_simbolos_tab.clear()
        try:
            procesar_instrucciones(instrucciones, ts, save=True)
            procesar_instrucciones(instrucciones, ts)
            self.tabla_simbolos_tab.append(ts.obtener_datos())
            self.consola_tab.append('\n'.join(resultados))
            self.errores_tab.append('\n'.join(errores))
            
        except Exception as e:
            errores.append("Error: ", e)
            print("Error: ", e)
            
    def Limpiar(self):
        self.consola_tab.clear()

    def mostrarReportes(self):
        QMessageBox.information(self, 'Mensaje', 'Reportes generados')
