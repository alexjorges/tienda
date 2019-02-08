from odoo import models, fields, api

class Facturas(models.Model):
    _name = 'tienda.facturas'
    cdFactura = fields.Integer('codigo Factura', required=True)
    fecha_actual = fields.Date(string='Fecha actual', default=lambda s: fields.Date.context_today(s))
    nombreCliente = fields.Many2one('tienda.cliente', 'Nombre Del Cliente')
    articulos = fields.Many2one('tienda.articulos', 'Articulos')
    cantidad = fields.Integer(related='articulos.cantidad', string='Cantidad')
    precio = fields.Integer(related='articulos.precio', string='Precio')
    total = fields.Float(string='Total', compute='_total')



    def name_get(self):
        res = []
        for record in self:
            name = record.nombreCliente
            res.append((record.id, name))
        return res

    @api.one
    @api.depends('precio', 'cantidad')
    def _total(self):
        self.total = self.precio * self.cantidad


