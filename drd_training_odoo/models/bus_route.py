from odoo import models, fields 

class BusRoute(models.Model):

    _name = 'bus.route'
    _description = 'Bus Route'
    
    name = fields.Char(string='Name')