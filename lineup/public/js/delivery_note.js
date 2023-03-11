frappe.ui.form.on("Delivery Note", {
	refresh: function(frm) {
		frm.set_query("contract_name", function(doc) {
			return {
				filters: {
					"party_name": doc.customer
				}
			}
		});
	}
});
