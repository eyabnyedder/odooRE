from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Estate(models.Model):
    # to indicate that this class should not be mapped to the database
    _name = "re.estate"
    _decription = "here contains all informations about your estate"

    surface = fields.Char(string='Surface', required=True, tracking=True)
    price = fields.Integer(string='Price', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    image = fields.Image(string="Image")
    type = fields.Selection([
        ('sale', 'Sale'),
        ('rent', 'Rent')
    ], string="Type", required=True, tracking=True)

    type_estate = fields.Selection([
        ('house', 'House'),
        ('ground', 'Ground')
    ], string="Type of estate", required=True, tracking=True)


    type_ground = fields.Char(string='Type', required=True, tracking=True)
    # the estate can have many images?
    description = fields.Text(string='Description', tracking=True)
    image = fields.Image(string="Image")

    # house properties
    floor_nbr = fields.Char(int='Floor_nbr', required=True, tracking=True)
    bedroom_nbr = fields.Char(int='Bedroom_nbr', required=True, tracking=True)
    bathroom_nbr = fields.Char(int='Bathroom_nbr', required=True, tracking=True)
    kitchen_nbr = fields.Char(int='Kitchen_nbr', required=True, tracking=True)
    garden_surface = fields.Char(int='garden_surface', tracking=True)

    # apartement number
    # house properties+ the fields below

    floor_num = fields.Char(int='Floor_num', required=True, tracking=True)

    # this number refers to its exact location
