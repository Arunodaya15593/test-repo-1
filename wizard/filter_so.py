# -*- coding: utf-8 -*-


from openerp import api, fields, models, _
from openerp.exceptions import UserError
from openerp import tools

class export_data(models.TransientModel):
	_name = 'filter.so.wizard' 	

	start = validity_date = fields.Datetime(string='Start Date')
	end = validity_date = fields.Datetime(string='End Date')

	@api.multi
	def filter_so(self):
		'''Search sale orders created between start and end'''

		if self.start > self.end:
			raise UserError("Please select a date in start after %s " %(self.start))
		else:
			action_so_tree_view = self.env.ref('sale.action_orders')
			domain  = eval(action_so_tree_view.domain)
			domain.append(('date_order', '>', self.start))
			domain.append(('date_order', '<', self.end))
			return {
	            'name': action_so_tree_view.name,
	            'help': action_so_tree_view.help,
	            'type': action_so_tree_view.type,
	            'view_type': action_so_tree_view.view_type,
	            'view_mode': action_so_tree_view.view_mode,
	            'search_view_id': action_so_tree_view.search_view_id.id,
	            'target': action_so_tree_view.target,
	            'context': action_so_tree_view.context,
	            'res_model': action_so_tree_view.res_model,
	            'domain': domain,
	        }