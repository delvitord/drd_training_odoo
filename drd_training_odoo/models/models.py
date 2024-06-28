-*- coding: utf-8 -*-

from odoo import models, fields 


class drd_training_odoo(models.Model):
    _name = 'some.model'
    _description = 'Some Description'
    
    name = fields.Char(string='Name')

    payment_method = fields.Selection([("cash","Cash"),("card","Card")], string='Payment Method')
    

    