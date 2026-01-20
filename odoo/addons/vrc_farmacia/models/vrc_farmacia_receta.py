from odoo import models, fields

class Receta(models.Model):
    _name = 'vrc_farmacia.receta'
    _description = 'Receta médica'

    name = fields.Char(string="Número de receta", required=True)
    fecha = fields.Date(string="Fecha")

    paciente_id = fields.Many2one(
        'vrc_farmacia.paciente',
        string="Paciente"
    )
    medicamento_ids = fields.Many2many(
        'vrc_farmacia.medicamento',
        relation = "vrc_rel_receta_medicamentos",
        string="Medicamentos"
    )

    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('entregada', 'Entregada')
    ], string="Estado", default='borrador')
