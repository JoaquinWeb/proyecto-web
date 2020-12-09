from typing import ByteString
from odoo import models, fields, api

class Bodega(models.Model):
    _name = 'inventarios.bodega'

    name = fields.Char(string="Nombre", required=True)
    value = fields.Integer(string="valor", required=True)
    quantity = fields.Integer(string="cantidad", required=True)
    date_register = fields.Date(string="fecha registro",required=True)
    description = fields.Text(string="descripcion")