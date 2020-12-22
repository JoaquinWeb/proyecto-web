
from odoo import models, fields, api

class RegistroInventario(models.Model):
    _name = 'inventarios.registro'
    cantidad_r = fields.Integer(string="cuantas unidades se retiran", required=True)

    nombre_id = fields.Char('Nombre', related='inventario_id.name') 
    inventario_id = fields.Many2one('inventarios.bodega', string='registro_id')
    