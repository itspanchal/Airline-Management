# Copyright (c) 2025, komal panchal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportTenant(Document):
	def validate(self):
		if self.tenant_contract_start_date >= self.tenant_contract_end_date:
			frappe.throw("Contract start date should be less than contract end date")
