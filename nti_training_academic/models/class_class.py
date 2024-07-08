from odoo import models, fields

class Class(models.Model):
    _name = 'class.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    user_id = fields.Many2one(
        comodel_name='res.users', 
        string='Responsible', 
        required=True
    )
    student_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Student', 
        domain=[('is_lecturer', '=', False)]
    )
    subject_line_ids = fields.One2many(
        comodel_name='subject.line', 
        inverse_name='class_id', 
        string='Subject Line'
    )
    
    