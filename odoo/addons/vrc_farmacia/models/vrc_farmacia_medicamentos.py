from odoo import models, fields

class Medicamento(models.Model):
    _name = 'vrc_farmacia.medicamento'
    _description = 'Medicamento'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del medicamento")
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock")
    imagen = fields.Image('imagen', max_width= 1920 , max_height= 1080)

    imagen = fields.Binary(string="Imagen del Medicamento")
    proveedor_id = fields.Many2one(
        'vrc_farmacia.proveedor',
        string="Proveedor"
    )
    receta_ids = fields.Many2many(
        'vrc_farmacia.receta',
        relation = "vrc_rel_receta_medicamentos",
        string="Recetas"
    )

