# -*- encoding: utf-8 -*-
##############################################################################
#
#    Module Writen to Odoo, Open Source Management Solution
#    
#    Copyright (C) 2013 Obertix Free Solutions (<http://obertix.net>).
#                       cubells <info@obertix.net>
#       
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published 
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################


from openerp.osv import fields, osv
from openerp.tools.translate import _

DOCUMENTS_DICT = {
    'purchase.order': 'date_order',
    'sale.order': 'date_order',
    'stock.picking.in': 'date',
    'stock.picking.out': 'date',
    'stock.picking': 'date',
    'account.invoice': 'date_invoice',
}

class SearchDocuments(osv.osv_memory):
    """
    This wizard will search documents by date
    """
    
    _name = "search.documents.dates"
    _description = "Search Documents by Date"
    
    _columns = {
        'date_from': fields.date('From date', required=True, select=True),
        'date_to': fields.date('To date', required=True, select=True),
    }
    
    _defaults = {
        'date_from': fields.date.context_today,
        'date_to': fields.date.context_today,
    }
    
    def search_document(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        
        active_model = context.get('active_model', False)
        model_obj = self.pool[active_model]
        ir_model_data = self.pool['ir.model.data']
        if active_model not in DOCUMENTS_DICT:
            raise osv.except_osv(_("Sorry !"), _("Option not available."))
        data = self.browse(cr, uid, ids[0], context=context)
        if data.date_from > data.date_to:
            raise osv.except_osv(_("It's a joke !"), 
                _("Final date has to be greater than initial date."))
        args = [
            (DOCUMENTS_DICT[active_model], '>=', data.date_from),
            (DOCUMENTS_DICT[active_model], '<=', data.date_to),
        ]
        model_ids = model_obj.search(cr, uid, args, context=context)  
        if not model_ids:
            raise osv.except_osv(_("No data !"), 
                _("There is not any document between the date range."))                                 
        return {
            'name': _('Documents between %s and %s' % \
                                        (data.date_from, data.date_to)),
            'view_type': 'form',
            'view_mode': 'form,tree',
            'res_model': active_model,
            'res_id': model_ids,
            'view_id': False,
            'views': [(False, 'tree')],
            'domain':[('id', 'in', model_ids)],
            'type': 'ir.actions.act_window',
        }
SearchDocuments()
