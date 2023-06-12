from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        index=True,
        ondelete='restrict',
        readonly=True,
        store=True,
        group_expand='_read_group_partner_id',
    )

    def _read_group_partner_id(self, partners, domain, order):
        return partners.search([], order=order)

