import csv
import os

class Library:
    def __init__(self):
        self.book_file = "book.csv"
        self.address_file = "address.csv"
        self.customer_file = "customer.csv"
        self.database_folder = "DATABASE"

    def register_customer(self):
        street = input("Podaj ulicę: ")
        city = input("Podaj miasto: ")
        country = input("Podaj kraj: ")

        with open(self.address_file, mode='r') as file:
            reader = csv.reader(file)
            lines = list(reader)
            if lines:
                last_id = int(lines[-1][0])
            else:
                last_id = 200

        with open(self.address_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([last_id + 1, street, city, country])

    def delete_customer(self):
        customer_id = input("Podaj ID klienta do usunięcia: ")
        with open(self.address_file, mode='r') as file:
            addresses = list(csv.reader(file))
        with open(self.address_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row for row in addresses if row[0] != customer_id)

        customer_folder = os.path.join(self.database_folder, str(customer_id))
        if os.path.exists(customer_folder):
            os.rmdir(customer_folder)

# Przykładowe użycie
library = Library()
library.register_customer()
library.delete_customer()