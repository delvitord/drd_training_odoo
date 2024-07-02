from odoo import models, fields, api

class Passenger(models.Model):
    
    _name = 'res.passenger'
    _description = 'Passenger'
    
    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    born_date = fields.Date(string='Born Date')
    route_ids = fields.Many2many('res.route', string='Route')
    age = fields.Integer(string='Age', compute='_compute_age')

    @api.depends('born_date')
    def _compute_age(self):
        for record in self:
            if record.born_date:
                record.age = fields.Date.today().year - record.born_date.year
            else:
                record.age = 0