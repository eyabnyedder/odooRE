from odoo import api, fields, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner']
    _ref_name = 'name'

