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

class ProductTemplate(osv.osv):
    _inherit = "product.template"
    _name = "product.template"

    _columns = {
	    'list_price': fields.float('Sale Price', 
	                    digits_compute=dp.get_precision('Product Cost'), 
	                    help="Base price for computing the customer price. \
	                                    Sometimes called the catalog price."),
        'standard_price': fields.float('Cost Price', required=True, 
                        digits_compute=dp.get_precision('Product Cost'), 
                        help="Product's cost for accounting stock valuation. \
                               It is the base price for the supplier price."),
    }

ProductTemplate()
