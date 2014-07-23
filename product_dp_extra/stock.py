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

class StockMove(osv.osv):
    _inherit = "stock.move"
    _name = "stock.move"

    _columns = {
    	'price_unit': fields.float('Unit Price', 
    	                digits_compute=dp.get_precision('Product Cost'), 
    	                        help="Technical field used to record \
    	                        the product cost set by the user during \
    	                        a picking confirmation (when average \
    	                        price costing method is used)"),
    }
	    
StockMove()
