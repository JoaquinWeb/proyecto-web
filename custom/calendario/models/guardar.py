from odoo import models, fields, api


class Calendario(models.Model):
    _name = 'calendario.guardar'

    date = fields.Date(string="fecha", required=True )
    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="descripcion", required=True)
    n_chacis = fields.Char(string="numero de chasis", required=True)