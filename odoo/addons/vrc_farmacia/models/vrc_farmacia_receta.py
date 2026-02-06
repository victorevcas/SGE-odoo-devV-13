from odoo import models, fields,api

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

    
    total_medicamentos = fields.Integer(
        string="Total medicamentos",
        compute="_compute_totales",
        store=True
    )


    coste_total = fields.Float(
        string="Coste total (€)",
        compute="_compute_totales",
        store=True
    )

 
    nombre_paciente = fields.Char(
        related="paciente_id.name",
        string="Nombre del paciente",
        store=True
    )


    @api.depends('medicamento_ids', 'medicamento_ids.precio')
    def _compute_totales(self):
        for receta in self:
            receta.total_medicamentos = len(receta.medicamento_ids)
            receta.coste_total = sum(m.precio for m in receta.medicamento_ids)
