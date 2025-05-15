import frappe
from frappe.utils import getdate

@frappe.background_job()
def update_ticket_gates(flight, new_gate_number):
    airline_tickets = frappe.get_all("Airline Ticket", filters={"flight": flight}, fields=["name"])
    for ticket in airline_tickets:
        frappe.db.set_value("Airline Ticket", ticket.name, "gate_number", new_gate_number)
    frappe.db.commit()

def send_rent_reminders():
    settings = frappe.get_single("Settings")
    if not settings.enable_rent_reminders:
        return

	current_month = getdate().strftime("%B %Y")
    shops = frappe.get_all("Airport Shop", fields=["name", "tenant", "rent_amount"])
    for shop in shops:
        tenant = frappe.get_doc("Tenant", shop.tenant)
        if tenant.email:
            frappe.sendmail(
                recipients=[tenant.email],
                subject= f"Rent Due Reminder for {current_month}",
                message=f"Dear {tenant.tenant_name}, your rent of ₹{shop.rent_amount} for Shop {shop.name} is due."
            )

def update_airport_shop_stats():
    airports = frappe.get_all("Airport", fields=["name"])
    for airport in airports:
        total = frappe.db.count("Airport Shop", {"airport": airport.name})
        occupied = frappe.db.count("Airport Shop", {"airport": airport.name, "tenant": ["is", "set"]})
        available = total - occupied

        frappe.db.set_value("Airport", airport.name, {
            "total_shops": total,
            "shops_occupied": occupied,
            "shops_available": available
        })
