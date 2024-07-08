from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age', store=True, readonly=True)
    is_lecturer = fields.Boolean(string='Is Lecturer', invisible=True)
    subject_line_ids = fields.One2many(comodel_name='subject.subject', inverse_name= 'lecturer_id', string='Subject Line', invisible=True)
    
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
