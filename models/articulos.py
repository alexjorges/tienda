from odoo import models, fields, api

class Articulos(models.Model):
    _name = 'tienda.articulos'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    precio = fields.Integer('Precio', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    proveedor = fields.Many2one('tienda.proveedores', 'Proveedores')

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res