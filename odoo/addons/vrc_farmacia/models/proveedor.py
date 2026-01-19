from odoo import models, fields

class Proveedor(models.Model):
    _name = 'farmacia.proveedor'
    _description = 'Proveedor'

    name = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono")
    medicamento_ids = fields.One2many(
        'farmacia.medicamento',
        'proveedor_id',
        string="Medicamentos"
    )
