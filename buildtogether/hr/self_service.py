import frappe


@frappe.whitelist()
def update_own_bank_details(bank, account_no, branch_code, account_type="Savings"):
	"""
	API: buildtogether/hr/self_service.py, POST
	Lets the logged-in employee update only their own bank details.
	"""
	employee = frappe.db.get_value(
		"Employee",
		{"user_id": frappe.session.user},
		"name"
	)

	if not employee:
		frappe.throw("No Employee record linked to your account.")

	doc = frappe.get_doc("Employee", employee)

	doc.bank_name = bank
	doc.bank_ac_no = account_no
	doc.custom_ifsc_code = branch_code
	doc.save(ignore_permissions=True)

	bank_account = frappe.db.get_value(
		"Bank Account",
		{"party_type": "Employee", "party": employee},
		"name"
	)

	return {"ok": True, "bank_account": bank_account}