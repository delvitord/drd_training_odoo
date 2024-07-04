from odoo import models, fields, api

class Bus(models.Model):
    _name = 'res.bus'
    _description = 'Bus'
    _sql_constraints = [
        ('bus_code_unique', 'unique(code)', 'Code must be unique')
    ]
    
    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity', required=True)
    image = fields.Binary(string='Image')
    
    schedule_ids = fields.One2many(comodel_name='bus.schedule', inverse_name='bus_id', string='Schedule')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('mt', 'Maintenance'),
        ('depart', 'Departure'),
    ], string='Status', default='draft', copy=False)
    
    def button_ready(self):
        self.state = 'ready'

    def button_mt(self):
        self.state = 'mt'

    def button_depart(self):
        self.state = 'depart'
