import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)
from blood_bank_management import BloodBankManagement

class BloodBankUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blood Bank Management")
        self.setGeometry(100, 100, 800, 600)

        self.blood_bank = BloodBankManagement()
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Add Donor Section
        add_donor_layout = QVBoxLayout()
        add_donor_groupbox = self.createGroupBox("Add Donor")
        add_donor_groupbox.setLayout(add_donor_layout)

        self.name_input = QLineEdit()
        self.blood_type_input = QLineEdit()
        self.phone_number_input = QLineEdit()
        self.city_input = QLineEdit()
        self.state_input = QLineEdit()

        add_donor_layout.addWidget(self.createLabel("Name:"))
        add_donor_layout.addWidget(self.name_input)
        add_donor_layout.addWidget(self.createLabel("Blood Type:"))
        add_donor_layout.addWidget(self.blood_type_input)
        add_donor_layout.addWidget(self.createLabel("Phone Number:"))
        add_donor_layout.addWidget(self.phone_number_input)
        add_donor_layout.addWidget(self.createLabel("City:"))
        add_donor_layout.addWidget(self.city_input)
        add_donor_layout.addWidget(self.createLabel("State:"))
        add_donor_layout.addWidget(self.state_input)

        add_donor_button = QPushButton("Add Donor")
        add_donor_button.clicked.connect(self.addDonor)
        add_donor_layout.addWidget(add_donor_button)

        # Search Donors Section
        search_donor_layout = QVBoxLayout()
        search_donor_groupbox = self.createGroupBox("Search Donors")
        search_donor_groupbox.setLayout(search_donor_layout)

        self.search_blood_type_input = QLineEdit()
        self.search_city_input = QLineEdit()
        self.search_state_input = QLineEdit()

        search_donor_layout.addWidget(self.createLabel("Blood Type:"))
        search_donor_layout.addWidget(self.search_blood_type_input)
        search_donor_layout.addWidget(self.createLabel("City:"))
        search_donor_layout.addWidget(self.search_city_input)
        search_donor_layout.addWidget(self.createLabel("State:"))
        search_donor_layout.addWidget(self.search_state_input)

        search_button = QPushButton("Search Donors")
        search_button.clicked.connect(self.searchDonors)
        search_donor_layout.addWidget(search_button)

        # Donor Table
        self.donor_table = QTableWidget()
        self.donor_table.setColumnCount(5)
        self.donor_table.setHorizontalHeaderLabels(["ID", "Name", "Blood Type", "Phone Number", "Location"])
        self.donor_table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.donor_table)

        main_layout.addWidget(add_donor_groupbox)
        main_layout.addWidget(search_donor_groupbox)

    def createLabel(self, text):
        label = QLabel(text)
        label.setFixedSize(100, 20)
        return label

    def createGroupBox(self, title):
        groupbox = QWidget()
        groupbox_layout = QVBoxLayout()
        groupbox.setLayout(groupbox_layout)

        label = QLabel(title)
        label.setStyleSheet("font-weight: bold;")
        groupbox_layout.addWidget(label)

        return groupbox

    def addDonor(self):
        name = self.name_input.text()
        blood_type = self.blood_type_input.text()
        phone_number = self.phone_number_input.text()
        city = self.city_input.text()
        state = self.state_input.text()
        
        self.blood_bank.add_donor(name, blood_type, phone_number, city, state)
        self.clearInputs()

    def clearInputs(self):
        self.name_input.clear()
        self.blood_type_input.clear()
        self.phone_number_input.clear()
        self.city_input.clear()
        self.state_input.clear()

    def searchDonors(self):
        blood_type = self.search_blood_type_input.text()
        city = self.search_city_input.text()
        state = self.search_state_input.text()

        donors = self.blood_bank.search_donors(blood_type, city, state)
        self.displayDonors(donors)

    def displayDonors(self, donors):
        self.donor_table.setRowCount(0)
        for row_num, row_data in enumerate(donors):
            self.donor_table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.donor_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BloodBankUI()
    window.show()
    sys.exit(app.exec_())
