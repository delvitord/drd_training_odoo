from odoo import models, fields 

class Passenger(models.Model):

    _name = 'res.passenger'
    _description = 'Passenger'
    
    name = fields.Char(string='Name', required=True)
    weight = fields.Float(string='Weight(Kg)', required=True)
    height = fields.Float(string='Height(Cm)', required=True)
    born_date = fields.Date(string='Born Date', required=True)