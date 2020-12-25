

from odoo import models, fields, api

class evaluacion(models.Model):
    _name = 'evaluacion'

    resultado = fields.Char(string="Nombre", required=True)
    repuestos = fields.Char(string="repuestos usados", required=True)
    
    

