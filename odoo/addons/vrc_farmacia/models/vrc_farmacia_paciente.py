from odoo import models, fields

class Paciente(models.Model):
    _name = 'vrc_farmacia.paciente'
    _description = 'Paciente'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    dni = fields.Char(string="DNI/Pasaporte")
    email = fields.Char(string="Correo Electrónico")
    imagen = fields.Image(string="Foto", max_width= 1920 , max_height= 1080)

    receta_ids = fields.One2many(
        'vrc_farmacia.receta',
        'paciente_id',
        string="Recetas"
    )
