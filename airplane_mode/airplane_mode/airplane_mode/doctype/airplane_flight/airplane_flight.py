# Copyright (c) 2025, komal panchal and contributors
# For license information, please see license.txt
# from xml.dom.minidom  Document
from frappe.model.document import Document
import frappe
from frappe.website.website_generator import WebsiteGenerator
from airplane_mode.tasks import update_ticket_gates


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"

	def on_update(self):
		if self.has_value_changed("gate_number"):
			update_ticket_gates(flight=self.name, new_gate_number=self.gate_number)

