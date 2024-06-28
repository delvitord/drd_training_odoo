# -*- coding: utf-8 -*-
# from odoo import http


# class DrdTrainingOdoo(http.Controller):
#     @http.route('/drd_training_odoo/drd_training_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drd_training_odoo/drd_training_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('drd_training_odoo.listing', {
#             'root': '/drd_training_odoo/drd_training_odoo',
#             'objects': http.request.env['drd_training_odoo.drd_training_odoo'].search([]),
#         })

#     @http.route('/drd_training_odoo/drd_training_odoo/objects/<model("drd_training_odoo.drd_training_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drd_training_odoo.object', {
#             'object': obj
#         })
