import frappe
import random
import string


def execute():
	data = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]},
							 fields=["name"])

	for airline_ticket in data:
		number = random.randint(1, 99)
		ascii_value = random.choice(string.ascii_uppercase)
		seat = f"{number}{ascii_value}"

		frappe.db.set_value("Airplane Ticket", airline_ticket.name, "seat", seat)
