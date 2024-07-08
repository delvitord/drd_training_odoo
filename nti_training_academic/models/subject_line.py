# Buat model subject_line dengan nama **subject.line** dengan list field sbb:
#     - subject_id - Many2one (subject.subject, required)
#     - lecturer_id - Many2one (res.partner, related=subject_id.lecturer_id)
#     - start_hour - float (widget float_time)
#     - end_hour - float (widget float_time)

from odoo import models, fields

class SubjectLine(models.Model):
    _name = 'subject.line'
    _description = 'Subject Line'

    subject_id = fields.Many2one('subject.subject', string='Subject', required=True)
    lecturer_id = fields.Many2one('res.partner', related='subject_id.lecturer_id', string='Lecturer')
    start_hour = fields.Float(string='Start Hour', widget='float_time')
    end_hour = fields.Float(string='End Hour', widget='float_time')
    class_id = fields.Many2one('class.class', string='Class')