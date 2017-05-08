// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

// -------------
// Menu Display
// -------------

// $(cur_frm.wrapper).on("grid-row-render", function(e, grid_row) {
// 	if(grid_row.doc && grid_row.doc.fieldtype=="Section Break") {
// 		$(grid_row.row).css({"font-weight": "bold"});
// 	}
// })

frappe.ui.form.on('DocType', {
	refresh: function(frm) {
		if(frm.doc.__islocal && (user !== "Administrator" || !frappe.boot.developer_mode)) {
			frm.set_value("custom", 1);
			frm.toggle_enable("custom", 0);
		}

		if(!frappe.boot.developer_mode && !frm.doc.custom) {
			// make the document read-only
			frm.set_read_only();
		}

		if(!frm.doc.__islocal) {
			frm.toggle_enable("engine", 0);
		}
	}
})

// for legacy... :)
cur_frm.cscript.validate = function(doc, cdt, cdn) {
	doc.server_code_compiled = null;
}
