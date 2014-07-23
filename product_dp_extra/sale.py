# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (c) 2010-2011 Elico Corp. All Rights Reserved.
#           Ian Li <ian.li@elico-corp.com>
#    Copyright (c) 2013 Obertix Free Solutions. All Rights Reserved.
#           cubells <vicent@vcubells.net>
#
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import decimal_precision as dp
from osv import fields, osv

class SaleOrderLine(osv.osv):
    _inherit = "sale.order.line"
    _name = "sale.order.line"

    _columns = {
    	'price_unit': fields.float('Unit Price', required=True, 
    	        digits_compute=dp.get_precision('Product Cost'), 
    	            readonly=True, states={'draft': [('readonly', False)]}),
    }
	
    def _prepare_order_line_invoice_line(self, cr, uid, line, 
                                            account_id=False, context=None):
        res = super(sale_order_line, 
                        self)._prepare_order_line_invoice_line(cr, uid, 
                                                line, account_id, context)
        
        def _get_line_qty(line):
            if (line.order_id.invoice_quantity=='order') or not line.procurement_id:
                if line.product_uos:
                    return line.product_uos_qty or 0.0
                return line.product_uom_qty
            else:
                return self.pool.get('procurement.order').quantity_get(cr, uid,
                        line.procurement_id.id, context=context)
        
        if not line.invoiced:
            uosqty = _get_line_qty(line)
            pu = 0.0
            if uosqty:
                pu = round(line.price_unit * line.product_uom_qty / uosqty,
                        self.pool.get('decimal.precision').precision_get(cr, uid, 'Product Cost'))
            
            res.update({'price_unit': pu})
	    return res
	    
SaleOrderLine()
