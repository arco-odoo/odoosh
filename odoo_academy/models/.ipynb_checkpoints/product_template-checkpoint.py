# -*- encoding: utf-8 -*-
from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_session_product = fields.Boolean(string='Use as Session Product',
                                        help='Check this box to use this as a product for the Session Fee',
                                        default=False)