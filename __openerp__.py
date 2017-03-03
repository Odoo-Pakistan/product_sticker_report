# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Product Sticker Report',
    'category': 'Product',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'depends': ['report', 'product'],
    'description': """
Product Sticker Report
======================
* Creates a QWeb report containing the name, code and EAN13 of a product
* Uses a custom 76x51mm paper format suitable for a sticker printer

""",
    'data': [
        'data/report_paperformat.xml',
        'views/product_sticker_template.xml',
        'report/product_sticker.xml',
    ],
}
