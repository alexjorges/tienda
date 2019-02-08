from odoo import models, fields, api

class Proveedores(models.Model):
    _name = 'tienda.proveedores'
    codigo = fields.Integer('codigo', required=True)
    nombre = fields.Char('nombre', required=True)
    direccion = fields.Char('direccion', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res