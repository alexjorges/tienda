from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'tienda.cliente'
    dni = fields.Integer('Dni', required=True)
    nombre = fields.Char('NombreCliente', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    cp = fields.Integer('Cp', required=True)
    direccion = fields.Char('Direccion', required=True)
    provincia = fields.Char('Provincia', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

    @api.one
    def limpiar(self):
        self.nombre = ""
        return True

    @api.multi
    def limpia_todo(self):
        self.dni = "0"
        self.nombre = ""
        self.apellidos = ""
        self.cp = "0"
        self.direccion = ""
        self.provincia = ""
        done_recs = self.search([('nombre', '=', 'fender')])
        done_recs.write({'nombre': 'Fender'})
        return True