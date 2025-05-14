# Copyright (c) 2025, komal panchal and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		print("========================")
		self.status = "Completed"
