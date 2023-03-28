frappe.ui.form.on("Sales Order", {
	refresh: function(frm) {
		frm.set_value("delivery_date", frappe.datetime.add_days(frm.doc.transaction_date, 15))
	}
});