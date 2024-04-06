import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

class DBMSManager(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('bloodbank.db')

        if not self.db.open():
            print("Error: Unable to connect to the database.")
            sys.exit(1)

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('sqlite_master')
        self.model.select()

        self.combo = QComboBox(self)
        self.combo.setModel(self.model)
        self.combo.setModelColumn(self.model.fieldIndex('name'))

        self.btn = QPushButton('Show Tables', self)
        self.btn.clicked.connect(self.show_tables)

        vbox = QVBoxLayout()
        vbox.addWidget(self.combo)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.setWindowTitle('DBMS Manager')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def show_tables(self):
        table_name = self.combo.currentText()
        print(f'Table Name: {table_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBMSManager()
    sys.exit(app.exec_())