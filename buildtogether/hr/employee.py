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


def sync_bank_account(doc, method):
	"""
	Employee on_update — create/link a Bank Account from employee bank details.
	Validates mandatory fields, enforces uniqueness (party + bank_account_no).
	"""
	if not (doc.bank_name and doc.bank_ac_no and doc.custom_ifsc_code):
		frappe.throw("Bank name, account number and IFSC code are mandatory")

	existing = frappe.db.get_value(
		"Bank Account", 
		{"party_type": "Employee", "party": doc.name},
		"name"
	)

	if existing:
		ba = frappe.get_doc("Bank Account", existing)
	else:
		ba = frappe.new_doc("Bank Account")

	ba.update({
		"party_type": "Employee",
		"party": doc.name,
		"account_name": doc.employee_name,
		"bank": doc.bank_name,
		"bank_account_no": doc.bank_ac_no,
		"branch_code": doc.custom_ifsc_code,
		"account_type": "Savings" 
	})
	ba.save(ignore_permissions=True) 

	doc.db_set("custom_bank_account", ba.name)

@frappe.whitelist()
def create_bank_account(employee):
	"""
	API: buildtogether/hr/employee.py, POST
	Idempotently create/link a Bank Account for the given employee.
	Reuses sync_bank_account logic to avoid duplicating create/link rules.
	"""
	doc = frappe.get_doc("Employee", employee)
	sync_bank_account(doc, "manual_api_call")

	bank_account = frappe.db.get_value(
		"Bank Account",
		{"party_type": "Employee", "party": employee},
		"name"
	)

	return {"bank_account": bank_account}
