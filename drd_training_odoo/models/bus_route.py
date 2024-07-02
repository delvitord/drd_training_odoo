from odoo import models, fields 

class BusRoute(models.Model):

    _name = 'bus.route'
    _description = 'Bus Route'
    
    name = fields.Char(string='Name', required=True)
    
    schedule_ids = fields.One2many(comodel_name='bus.schedule', inverse_name='route_id', string='Schedule')