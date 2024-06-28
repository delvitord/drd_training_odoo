-*- coding: utf-8 -*-

from odoo import models, fields

class HrEmployee(models.Model):
    """
    Menambahkan dependensi modul hr. Lalu tambahkan field berikut ini pada model hr.employee. 
        a. is_driver -> Type: Boolean, String: Is Driver
    """
    
    _inherit = 'hr.employee'

    is_driver = fields.Boolean(string='Is Driver')