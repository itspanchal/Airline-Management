# Copyright (c) 2025, komal panchal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShop(Document):
	def before_insert(self):
		if not self.rent_amount:
			settings = frappe.get_single("Settings")
			self.rent_amount = settings.default_rent_amount

	def validate(self):
		if self.shop_contract_start_date >= self.shop_contract_end_date:
			frappe.throw("Contract start date should be less than contract end date")

