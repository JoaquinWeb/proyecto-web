

from odoo import models, fields, api

class cliente(models.Model):
    _name = 'gep.cliente'

    nombre = fields.Char(string="Nombre", required=True)
    patente = fields.Char(string="patente", required=True)
    vehiculo = fields.Text(string="Nombre", required=True)
    
    
    proyecto_id = fields.Many2one('gep.proyecto', string="gep_cliente")
   