from odoo import models, fields, api

class Bus(models.Model):
    """
    Buat Model Bus dengan technical name res.bus memiliki rincian field sebagai berikut: 
        a. name -> Type: Char, String: Name 
        b. code -> Type: Char, String: Code 
        c. capacity -> Type: Integer, String: Capacity 
        d. image ->Type: Binary, String: Image
    """
    
    _name = 'res.bus'
    _description = 'Bus'
    
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity')
    image = fields.Binary(string='Image')
    schedule_ids = fields.One2many('bus.schedule', 'bus_id', string='Schedule')    

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('res.bus') or '/'
        return super(Bus, self).create(vals)
    