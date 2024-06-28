from odoo import models, fields 

class Passenger(models.Model):
    """
    Buat Model Passenger dengan technical name res.passenger memiliki rincian field sebagai berikut:
        a. name -> Type: Char, String: Name 
        b. weight -> Type: Float, String: Weight(Kg) 
        c. height -> Type: Float, String: Height(Cm) 
        d. born_date -> Type: Date, String: Born Date
    """
    
    _name = 'res.passenger'
    _description = 'Passenger'
    
    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    born_date = fields.Date(string='Born Date')