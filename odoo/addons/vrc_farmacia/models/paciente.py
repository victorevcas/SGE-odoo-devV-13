from odoo import models, fields

class Paciente(models.Model):
    _name = 'farmacia.paciente'
    _description = 'Paciente'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    dni = fields.Char(string="DNI/Pasaporte")
    email = fields.Char(string="Correo Electrónico")
    receta_ids = fields.One2many(
        'farmacia.receta',
        'paciente_id',
        string="Recetas"
    )
