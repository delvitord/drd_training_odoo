# -*- coding: utf-8 -*-
# from odoo import http


# class NtiTrainingAcademic(http.Controller):
#     @http.route('/nti_training_academic/nti_training_academic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nti_training_academic/nti_training_academic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nti_training_academic.listing', {
#             'root': '/nti_training_academic/nti_training_academic',
#             'objects': http.request.env['nti_training_academic.nti_training_academic'].search([]),
#         })

#     @http.route('/nti_training_academic/nti_training_academic/objects/<model("nti_training_academic.nti_training_academic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nti_training_academic.object', {
#             'object': obj
#         })
