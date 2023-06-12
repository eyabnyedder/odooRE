from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'PatientProfile'
    _ref_name = 'name'

    title = fields.Many2one('res.partner.title', string="Title")
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is child ?", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender", required=True, default='male', tracking=True)
    note = fields.Text(string='description', tracking=True)
    capitalized_name = fields.Char(string="Capitalized Name", compute='_compute_capitalized_name')
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    image = fields.Image(string="Image")
    partner_id = fields.Many2one('res.partner', string="Related Partner")

    def create_invoice(self):
        partners = self.env['res.partner']
        partner_id = partners.search([('name', '=', self.name)])
        if not partner_id:
            partner_id = partners.create({'name': self.name})

        invoice_vals = {
            "move_type": "out_invoice",
            "partner_id": partner_id.id,
            "company_id": self.env.company.id,
            "currency_id": self.env.company.currency_id.id,
            "journal_id": self.env["account.journal"].search([("type", "=", "sale")],limit=1,).id,
        }

        invoice = self.env["account.move"].create(invoice_vals)

        return {
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('account.view_move_form').id,
            'res_id': invoice.id,
        }


    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.constrains('is_child', 'age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)
