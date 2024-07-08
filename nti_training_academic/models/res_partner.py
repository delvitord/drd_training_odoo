from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age', store=True, readonly=True)
    is_lecturer = fields.Boolean(string='Is Lecturer')
    subject_line_ids = fields.One2many('subject.subject', 'lecturer_id', string='Subject Line')
    class_ids = fields.Many2many('class.class', string='Classes')
    
    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                today = fields.Date.today()
                rec.age = today.year - rec.birthday.year - ((today.month, today.day) < (rec.birthday.month, rec.birthday.day))
            else:
                rec.age = 0
                
    def button_subject_lines(self):
        return {
            'name': 'Subject Lines',
            'type': 'ir.actions.act_window',
            'res_model': 'subject.subject',
            'view_mode': 'tree',
            'view_type': 'tree',
            'domain': [('lecturer_id', '=', self.id)],
            'target': 'new',
        }
