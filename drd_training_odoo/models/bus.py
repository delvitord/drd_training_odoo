from odoo import models, fields, _

class Bus(models.Model):

    _name = 'res.bus'
    _description = 'Bus'
    _sql_constraints = [
        ('bus_code_unique', 'unique(code)', 'Code must be unique')
    ]
    _inherit = ['mail.thread','mail.activity.mixin']
    
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
        
    def report_bus_problem(self):
        return {
            'name': 'Bus Problem',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'report.bus.problem.wizard',
            'type': 'ir.actions.act_window',
            'context': {
                'default_bus_id': self.id
            },
            'target': 'new',
        }