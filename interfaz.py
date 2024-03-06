from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QTabWidget, QTextBrowser, QMessageBox, QFileDialog
from simbolos import TablaSimbolos
from funciones import *
import gramatica as g


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

        menubar.addMenu('Editar')

        menubar.addMenu('Descargar')

        # Recuadro para escribir
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 30, 400, 400)
        self.text_edit.setStyleSheet(
            "background-color: #072541; color: #ffffff; font-family: Arial; font-size: 12pt;")

        # Botones Ejecutar y Mostrar reportes
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

        tabla_simbolos_tab = QTextBrowser()
        tab_widget.addTab(tabla_simbolos_tab, 'Tabla de Símbolos')
        tabla_simbolos_tab.setStyleSheet(
            "background-color: #000000; color: #ffffff; font-family: Arial; font-size: 12pt;")
        tabla_simbolos_tab.setFixedSize(348, 375)

        errores_tab = QTextBrowser()
        tab_widget.addTab(errores_tab, 'Errores')
        errores_tab.setStyleSheet(
            "background-color: #000000; color: #ffffff; font-family: Arial; font-size: 12pt;")
        errores_tab.setFixedSize(348, 375)

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
        texto = self.text_edit.toPlainText()
        instrucciones = g.parse(texto)
        # instrucciones = g.parse(texto)
        ts = TablaSimbolos()
        try:
            resultado = procesar_instrucciones(instrucciones, ts)
            self.consola_tab.append(resultado)
            QMessageBox.information(self, 'Mensaje', 'Ejecucion finalizada')
        except Exception:
            print("Error")

    def mostrarReportes(self):
        QMessageBox.information(self, 'Mensaje', 'Reportes generados')
