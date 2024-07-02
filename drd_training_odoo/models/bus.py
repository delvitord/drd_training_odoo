from odoo import models, fields 

class Bus(models.Model):

    _name = 'res.bus'
    _description = 'Bus'
    _sql_constraints = [
        ('bus_code_unique', 'unique(code)', 'Code must be unique')
    ]
    
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity')
    image = fields.Binary(string='Image')
    
    schedule_ids = fields.One2many(comodel_name='bus.schedule', inverse_name='bus_id', string='Schedule')
    