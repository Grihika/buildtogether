import frappe
from frappe import _

def enforce_interviewer(doc, method):
    if doc.docstatus == 1 and doc.interviewer != frappe.session.user:
        frappe.throw(_("Only the specifically assigned interviewer can submit this feedback."))

def sync_applicant_status(doc, method):
    if doc.result == "Cleared":
        frappe.db.set_value("Job Applicant", doc.job_applicant, "status", "Cleared")
        frappe.db.set_value("Job Applicant", doc.job_applicant, "workflow_state", "Cleared")