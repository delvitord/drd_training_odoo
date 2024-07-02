from odoo import models, fields

class Baggage(models.Model):
    
    _name = 'baggage.baggage'
    _description = 'Baggage'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight (Kg)')
    schedule_id = fields.Many2one(comodel_name='bus.schedule', string='Schedule')