from odoo import models, fields, api

class Almacen(models.Model):
    _name = 'tienda.almacen'
    direccion = fields.Char('Direccion', required=True)
    cp = fields.Integer('Cp', required=True)
    nombre = fields.Integer('Nombre', required=True)
    telefono = fields.Integer('Telefono',required=True)
    articulo = fields.Many2one('tienda.articulos','Articulos')

    def name_get(self):
        res = []
        for record in self:
            nombre = record.nombre
            res.append((record.id, nombre))
        return res
