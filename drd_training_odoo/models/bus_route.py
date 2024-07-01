from odoo import models, fields 

class BusRoute(models.Model):
    """
    Buat Model Bus Route dengan technical name bus.route memiliki rincian field sebagai berikut:
        a. name -> Type: Char, String: Name 
    """
    
    _name = 'bus.route'
    _description = 'Bus Route'
    
    name = fields.Char(string='Name')
    passenger_ids = fields.Many2many('res.passenger', string='Passenger')