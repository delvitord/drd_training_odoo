from odoo import models, fields 

class BusSchedule(models.Model):
    """
    Buat Model Bus Schedule dengan technical.name bus.schedule rincian field sebagai berikut:
        a. name -> Type: Char, String: Name 
        b. schedule -> Type: Datetime, String: Schedule 
        c. payment_type -> Type: Selection, String: Payment, Selection: [(“cash”, “Cash”), (“transfer”, “Transfer”)] 
        d. departure -> Type: Datetime, String: Departure 
        e. arrival -> Type: Datetime, String: Arrival
    """
    
    _name = 'bus.schedule'
    _description = 'Bus Schedule'
    
    name = fields.Char(string='Name')
    schedule = fields.Datetime(string='Schedule')
    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ], string='Payment')
    departure = fields.Datetime(string='Departure')
    arrival = fields.Datetime(string='Arrival')