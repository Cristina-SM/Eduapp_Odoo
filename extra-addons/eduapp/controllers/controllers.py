# -*- coding: utf-8 -*-
# from odoo import http


# class Eduapp(http.Controller):
#     @http.route('/eduapp/eduapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eduapp/eduapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eduapp.listing', {
#             'root': '/eduapp/eduapp',
#             'objects': http.request.env['eduapp.eduapp'].search([]),
#         })

#     @http.route('/eduapp/eduapp/objects/<model("eduapp.eduapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eduapp.object', {
#             'object': obj
#         })
