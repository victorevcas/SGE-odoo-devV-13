from odoo import models, fields

class Medicamento(models.Model):
    _name = 'farmacia.medicamento'
    _description = 'Medicamento'

    name = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock")
    proveedor_id = fields.Many2one(
        'farmacia.proveedor',
        string="Proveedor"
    )
    receta_ids = fields.Many2many(
        'farmacia.receta',
        string="Recetas"
    )
