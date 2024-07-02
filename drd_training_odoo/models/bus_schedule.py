from odoo import models, fields, api

class BusSchedule(models.Model):

    
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
    bus_id = fields.Many2one('res.bus', string='Bus')
    
    day_until_departure = fields.Integer(string='Day Until Departure', compute='_compute_day_until_departure')
    
    @api.depends('departure')
    def _compute_day_until_departure(self):
        for rec in self:
            rec.day_until_departure = 0
            if rec.departure:
                rec.day_until_departure = (rec.departure - fields.Datetime.now()).days                