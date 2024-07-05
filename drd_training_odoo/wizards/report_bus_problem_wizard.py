from odoo import models, fields

class ReportBusProblemWizard(models.TransientModel):
    _name = 'report.bus.problem.wizard'
    _description = 'Wizard to report bus problems'

    bus_id = fields.Many2one(
        comodel_name='res.bus',
        string="Bus",
    )
    reason = fields.Text(string='Problem Description')

    def report_problem(self):
        self.bus_id.state = 'mt'
        message_body = "Problem: " + self.reason
        self.bus_id.message_post(body=message_body)
        return {'type': 'ir.actions.act_window_close'}