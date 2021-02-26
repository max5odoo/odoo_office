# -*- coding: utf-8 -*-
# from odoo import http


# class NewApp(http.Controller):
#     @http.route('/new_app/new_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_app/new_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_app.listing', {
#             'root': '/new_app/new_app',
#             'objects': http.request.env['new_app.new_app'].search([]),
#         })

#     @http.route('/new_app/new_app/objects/<model("new_app.new_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_app.object', {
#             'object': obj
#         })
