import frappe


def validate_names(doc, method):
	"""
	Allow single-name Employee records (last_name optional).
	Safely build employee_name from whatever name parts exist.
	"""
	name_parts = [doc.first_name, doc.middle_name, doc.last_name]
	full_name = " ".join(part.strip() for part in name_parts if part and part.strip())

	if not full_name:
		frappe.throw("Employee must have at least a First Name.")

	doc.employee_name = full_name 