from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SubjectLine(models.Model):
    _name = 'subject.line'
    _description = 'Subject Line'

    subject_id = fields.Many2one(comodel_name='subject.subject', string='Subject', required=True)
    lecturer_id = fields.Many2one(comodel_name='res.partner', related='subject_id.lecturer_id', string='Lecturer')
    start_hour = fields.Float(string='Start Hour', widget='float_time')
    end_hour = fields.Float(string='End Hour', widget='float_time')
    class_id = fields.Many2one(comodel_name='class.class', string='Class')
    
    # Function untuk cek format start hour
    @api.onchange('start_hour')
    def _check_start_hour_format(self):
        for record in self:
            if record.start_hour:
                try:
                    hour, minute = divmod(record.start_hour * 60, 60)
                    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                        raise ValidationError("Invalid start hour format. Please use HH:MM format.")
                except Exception:
                    raise ValidationError("Invalid start hour format. Please use HH:MM format.")

    # Function untuk cek format end hour
    @api.onchange('end_hour')
    def _check_end_hour_format(self):
        for record in self:
            if record.end_hour:
                try:
                    hour, minute = divmod(record.end_hour * 60, 60)
                    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                        raise ValidationError("Invalid end hour format. Please use HH:MM format.")
                except Exception:
                    raise ValidationError("Invalid end hour format. Please use HH:MM format.")
                
    # Function untuk cek start hour < end hour
    @api.onchange('start_hour', 'end_hour')
    def _check_start_end_hour(self):
        for record in self:
            if record.start_hour and record.end_hour:
                if record.start_hour >= record.end_hour:
                    raise ValidationError("Start hour must be less than end hour.")
                
    # Function untuk cek apakah jadwal overlapping atau 
    @api.constrains('start_hour', 'end_hour', 'class_id')
    def _validate_time_conflict(self):
        for record in self:
            if record.start_hour and record.end_hour and record.class_id:
                overlapping_subjects = self.env['subject.line'].search([
                    ('class_id', '=', record.class_id.id),
                    ('id', '!=', record.id),
                    ('start_hour', '<', record.end_hour),
                    ('end_hour', '>', record.start_hour)
                ])
                if overlapping_subjects:
                    raise ValidationError("The subject time conflicts with another subject in the same class.")
    
    # Function untuk menampilkan format time di report
    @api.model
    def float_to_time(self, float_val):
        hours, remainder = divmod(float_val * 60, 60)
        return "%02d:%02d" % (int(hours), int(remainder))