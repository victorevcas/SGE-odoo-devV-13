from odoo import models, fields

class Receta(models.Model):
    _name = 'farmacia.receta'
    _description = 'Receta médica'

    name = fields.Char(string="Número de receta", required=True)
    fecha = fields.Date(string="Fecha")

    paciente_id = fields.Many2one(
        'farmacia.paciente',
        string="Paciente"
    )
    medicamento_ids = fields.Many2many(
        'farmacia.medicamento',
        string="Medicamentos"
    )

    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('entregada', 'Entregada')
    ], string="Estado", default='borrador')
