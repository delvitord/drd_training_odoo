from odoo import models, fields, api

class Passenger(models.Model):

    _name = 'res.passenger'
    _description = 'Passenger'
    
    name = fields.Char(string='Name', required=True)
    weight = fields.Float(string='Weight(Kg)', required=True)
    height = fields.Float(string='Height(Cm)', required=True)
    born_date = fields.Date(string='Born Date', required=True)
    
    age = fields.Integer(string='Age', compute='_compute_age')

    @api.depends('born_date')
    def _compute_age(self):
        for rec in self:
            if rec.born_date:
                today = fields.Date.today()
                age = today.year - rec.born_date.year - ((today.month, today.day) < (rec.born_date.month, rec.born_date.day))
                rec.age = age
            else:
                rec.age = 0