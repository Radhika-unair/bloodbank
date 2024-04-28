import mysql.connector

class BloodBankManagement:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="bloodbank"
        )
        self.cursor = self.conn.cursor()

    def add_donor(self, name, blood_type, phone_number, city, state):
        query = "INSERT INTO Donors (name, blood_type, phone_number, city, state) VALUES (%s, %s, %s, %s, %s)"
        values = (name, blood_type, phone_number, city, state)
        self.cursor.execute(query, values)
        self.conn.commit()

    def add_blood(self, blood_type, quantity):
        query = "INSERT INTO BloodInventory (blood_type, quantity) VALUES (%s, %s) ON DUPLICATE KEY UPDATE quantity = quantity + %s"
        values = (blood_type, quantity, quantity)
        self.cursor.execute(query, values)
        self.conn.commit()

    def search_donors(self, blood_type, city=None, state=None):
        query = "SELECT * FROM Donors WHERE blood_type = %s"
        params = [blood_type]

        if city:
            query += " AND city = %s"
            params.append(city)
        if state:
            query += " AND state = %s"
            params.append(state)

        self.cursor.execute(query, tuple(params))
        return self.cursor.fetchall()

    def get_blood_inventory(self):
        query = "SELECT * FROM BloodInventory"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Example usage
blood_bank = BloodBankManagement()
blood_bank.add_donor("John Doe", "O+", "1234567890", "New York", "NY")
blood_bank.add_blood("O+", 10)
print(blood_bank.search_donors("O+"))
print(blood_bank.get_blood_inventory())
blood_bank.close_connection()
