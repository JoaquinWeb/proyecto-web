# -*- coding: utf-8 -*-
from odoo import http

# class Gep(http.Controller):
#     @http.route('/gep/gep/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gep/gep/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gep.listing', {
#             'root': '/gep/gep',
#             'objects': http.request.env['gep.gep'].search([]),
#         })

#     @http.route('/gep/gep/objects/<model("gep.gep"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gep.object', {
#             'object': obj
#         })