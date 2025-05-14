import frappe
from frappe import _
from frappe.utils.password import update_password


@frappe.whitelist()
def update_passwords(email, password):

	if not frappe.db.exists("User", email):
		frappe.throw(_("User not found"))

	if not email.lower() == "administrator":
		update_password(email, password)

	return {"message": _("Password updated successfully for user {0}").format(email)}



# Api Secret: 2b3a3acfe55933e
# Api key : cee43e2cb262c29

