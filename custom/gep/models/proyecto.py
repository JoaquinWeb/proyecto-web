

from odoo import models, fields, api

class proyecto(models.Model):
    _name = 'gep.proyecto'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="descripcion")
    fecha = fields.Date(string="fecha de registros", required=True)
    mecanico = fields.Char(string="Nombre", required=True)
    
    
    evaluacion_id = fields.Many2one('gep.evaluacion', string="gep_proyecto")