

from odoo import models, fields, api

class cliente(models.Model):
    _name = 'cliente.proyecto'

    nombre = fields.Char(string="Nombre", required=True)
    patente = fields.Char(string="patente", required=True)
    vehiculo = fields.Text(string="Nombre", required=True)
    
    
    proyecto_id = fields.Many2one('cliente.proyecto_gep', string="gep_cliente")
   