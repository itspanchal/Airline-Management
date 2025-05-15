# Copyright (c) 2025, komal panchal and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
import random
import string


class AirplaneTicket(Document):


	# Set the rendom string in the seat field
	def before_insert(self):
		number = random.randint(1,99)
		ascii_value = random.choice(string.ascii_uppercase.upper())
		# print(f'{ number}{ascii_value}')
		self.seat = f'{ number}{ascii_value}'

		flight = frappe.get_doc("Airplane Flight", self.flight)

		airplane = frappe.get_doc("Airplane", flight.airplane)
		airplane_capacity = airplane.capacity

		tickets_count = frappe.db.count("Airplane Ticket", {
			"flight": self.flight,
			"docstatus": ["!=", 2]
		})


		if tickets_count >= airplane_capacity:
			frappe.throw(_("Oops! Ticket not available for this flight").format(
				airplane.name, airplane_capacity
			))


	# calculate the total amount and populate before the save
	def before_save(self):
		add_ons_item_total = sum(
			add_ons_amount.get("amount", 0) for add_ons_amount in self.add_ons)
		self.total_amount = self.flight_price + add_ons_item_total

		if self.flight:
			flight = frappe.get_doc("Airplane Flight", self.flight)

			self.gate_number = flight.gate_number



	# Remove duplicate add_ons value
	def validate(self):
		if self.docstatus == 0:
			new_add_ons = []
			item_names = []

			for add_on in self.add_ons:
				if add_on.item not in item_names:
					item_names.append(add_on.item)
					new_add_ons.append(add_on)
				else:
					frappe.msgprint("Delete the duplicate add_on value")
			self.add_ons = new_add_ons


	# Checked the TicketStatus before the submit Airline ticket.
	def before_submit(self):
		import pdb;pdb.set_trace()
		if self.ticketstatus == "Boarded":
			frappe.throw(_("Ticket is already boarded"))









