# -*- coding: utf-8 -*-

from odoo import models, fields, api

class inventarios(models.Model):
    _name = 'inventarios.bodega'

    name = fields.Char(string="Nombre", required=True)
    value = fields.Integer(string="Valor", required=True)
    quantity = fields.Integer(string="Cantidad", required=True)
    date_register = fields.Date(string="fecha de registros", required=True)
    description = fields.Text(string="descripcion")
    
    
    proveedor_id = fields.Many2one('inventarios.bodega_proveedor', string="nombre proveedor")

