from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BusSchedule(models.Model):

    _name = 'bus.schedule'
    _description = 'Bus Schedule'
    
    name = fields.Char(string='Name', required=True)
    date_of_issue = fields.Date(string='Schedule', default=fields.Datetime.now, readonly=True)
    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ], string='Payment')
    departure = fields.Datetime(string='Departure', required=True)
    arrival = fields.Datetime(string='Arrival', required=True)
    
    baggage_ids = fields.One2many(comodel_name='baggage.baggage', inverse_name='schedule_id', string='Baggage')
    bus_id = fields.Many2one(comodel_name='res.bus', string='Bus', required=True)
    route_id = fields.Many2one(comodel_name='bus.route', string='Route', required=True)
    passenger_ids = fields.Many2many(comodel_name='res.passenger', string='Passenger')
    capacity = fields.Integer(string='Capacity', related='bus_id.capacity', readonly=True)
        
    @api.constrains('departure', 'arrival')
    def _check_departure_arrival(self):
        for record in self:
            if record.departure and record.arrival and record.departure > record.arrival:
                raise ValidationError("Arrival cannot be earlier than Departure.")
            
    @api.constrains('passenger_ids')
    def _check_passenger_capacity(self):
        for record in self:
            if record.passenger_ids and len(record.passenger_ids) > record.capacity:
                raise ValidationError("Passenger count exceeds bus capacity.")
            
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('bus.schedule')
        return super(BusSchedule, self).create(vals)