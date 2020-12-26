

from odoo import models, fields, api

class inventariosProveedor(models.Model):
    _name = 'inventarios.bodega_proveedor'

    name = fields.Char(string="Nombre", required=True)
    city = fields.Char(string="Ciudad", required=True)
    address = fields.Char(string="direccion", required=True)
    first_register = fields.Date(string="primer registro", required=True)
    number_cel = fields.Integer(string="Telefono", required=True)
    

    image = fields.Binary(string='Imagen')