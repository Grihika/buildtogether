app_name = "buildtogether"
app_title = "BuildTogether"
app_publisher = "aman@buildtogether.co.in"
app_description = "This is the app customising the requirements of BuildTogether"
app_email = "aman@buildtogether.co.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "buildtogether",
# 		"logo": "/assets/buildtogether/logo.png",
# 		"title": "BuildTogether",
# 		"route": "/buildtogether",
# 		"has_permission": "buildtogether.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/buildtogether/css/buildtogether.css"
# app_include_js = "/assets/buildtogether/js/buildtogether.js"

# include js, css files in header of web template
# web_include_css = "/assets/buildtogether/css/buildtogether.css"
# web_include_js = "/assets/buildtogether/js/buildtogether.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "buildtogether/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "buildtogether/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "buildtogether.utils.jinja_methods",
# 	"filters": "buildtogether.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "buildtogether.install.before_install"
# after_install = "buildtogether.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "buildtogether.uninstall.before_uninstall"
# after_uninstall = "buildtogether.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "buildtogether.utils.before_app_install"
# after_app_install = "buildtogether.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "buildtogether.utils.before_app_uninstall"
# after_app_uninstall = "buildtogether.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "buildtogether.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "buildtogether.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Employee": {
        "validate": "buildtogether.hr.employee.validate_names",
        "on_update": "buildtogether.hr.employee.sync_bank_account"
    },
    "Interview Feedback": {
        "validate": "buildtogether.recruitment.feedback.enforce_interviewer",
        "on_submit": "buildtogether.recruitment.feedback.sync_applicant_status"
    }
}

fixtures = [
    {
        "dt": "BuildTogether Settings"
    },
    {
        "dt": "Custom Field",
        "filters": [["name", "in", [
            "Employee-custom_ifsc_code",
            "Employee-custom_bank_account",
            "Employee-custom_biometric_id"
        ]]]
    },
    {
        "dt": "Property Setter",
        "filters": [["doc_type", "in", ["Employee", "Bank Account", "Payroll Entry"]]]
        "filters": [["doc_type", "in", ["Employee", "Bank Account"]]]
    },
    {
        "dt": "Web Form",
        "filters": [["name", "=", "employee-onboarding"]]
    }
] 
 
# --------------- 

# scheduler_events = {
# 	"all": [
# 		"buildtogether.tasks.all"
# 	], 
# 	"daily": [
# 		"buildtogether.tasks.daily"
# 	],
# 	"hourly": [
# 		"buildtogether.tasks.hourly"
# 	],
# 	"weekly": [
# 		"buildtogether.tasks.weekly"
# 	],
# 	"monthly": [
# 		"buildtogether.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "buildtogether.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "buildtogether.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "buildtogether.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "buildtogether.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["buildtogether.utils.before_request"]
# after_request = ["buildtogether.utils.after_request"]

# Job Events
# ----------
# before_job = ["buildtogether.utils.before_job"]
# after_job = ["buildtogether.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"buildtogether.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

