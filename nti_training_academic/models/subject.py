from odoo import models, fields

class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image')
    code = fields.Char(string='Code', required=True)
    lecturer_id = fields.Many2one(comodel_name='res.partner', string='Lecturer', domain=[('is_lecturer', '=', True)])