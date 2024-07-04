from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BusSchedule(models.Model):

    _name = 'bus.schedule'
    _description = 'Bus Schedule'
    _inherit = ['mail.thread','mail.activity.mixin']
        
    name = fields.Char(string='Name', required=True)
    date_of_issue = fields.Date(string='Schedule', default=fields.Datetime.now, readonly=True, tracking=True)
    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ], string='Payment', tracking=True)
    departure = fields.Datetime(string='Departure', required=True, tracking=True)
    arrival = fields.Datetime(string='Arrival', required=True, tracking=True)
    
    baggage_ids = fields.One2many(
        comodel_name='baggage.baggage', 
        inverse_name='schedule_id', 
        string='Baggage'
    )
    bus_id = fields.Many2one(
        comodel_name='res.bus', 
        string='Bus', 
        required=True, 
        tracking=True,
        domain=[('state', '=', 'ready')]
    )
    route_id = fields.Many2one(
        comodel_name='bus.route', 
        string='Route', 
        required=True
    )
    passenger_ids = fields.Many2many(
        comodel_name='res.passenger', 
        string='Passenger'
    )
    capacity = fields.Integer(
        string='Capacity', 
        related='bus_id.capacity', 
        readonly=True
    )
    driver_id = fields.Many2one(
        comodel_name='hr.employee', 
        string='Driver', 
        domain=[('is_driver', '=', True)], 
        tracking=True
    )
    is_driver = fields.Boolean(string='Is Driver', related='driver_id.is_driver')
    driver_license = fields.Char(string='Driver License', related='driver_id.driver_license')
    driver_license_expired_date = fields.Date(string='Driver License Expired Date', related='driver_id.driver_license_expired_date')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('ongoing', 'On Going'),
        ('done', 'Done'),
    ], string='Status', default='draft', copy=False)
    
        
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
    
    def button_submit(self):
        self.state = 'submit'
        if self.bus_id:
            self.bus_id.state = 'ready'

    def button_run(self):
        self.state = 'ongoing'
        if self.bus_id:
            self.bus_id.state = 'depart'

    def button_done(self):
        self.state = 'done'
        if self.bus_id:
            self.bus_id.state = 'draft'
    
    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'submit':
            if self.bus_id:
                self.bus_id.state = 'ready'
        elif self.state == 'ongoing':
            if self.bus_id:
                self.bus_id.state = 'depart'
        elif self.state == 'done':
            if self.bus_id:
                self.bus_id.state = 'mt'
    