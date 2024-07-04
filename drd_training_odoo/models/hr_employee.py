from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_driver = fields.Boolean(string='Is Driver')
    
    schedule_ids = fields.One2many(comodel_name='bus.schedule', inverse_name='driver_id', string='Schedule')
    driver_license = fields.Char(string='Driver License')
    driver_license_expired_date = fields.Date(string='Driver License Expired Date')
