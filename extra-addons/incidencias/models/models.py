# -*- coding: utf-8 -*-
from odoo import models, fields, api


class incidencias_inicendias(models.Model):
    _name = 'incidencias.incidencias'
    _descripcion = 'incidencias.incidencias'
    

    name = fields.Integer(string="Número incidencias")
    municipio = fields.Many2one("incidencias.municipios", string="Municipio", required=True, ondelete="cascade")
    fecha = fields.Date(string="Fecha")
    descripcion = fields.Char(string="Usuario que atiende la incidencias.")
    cliente = fields.Many2one("res.partner",string = "cliente", required=True, ondelete="cascade")

class incidencias_municipios(models.Model):
    _name='incidencias.municipios'
    _descripcion = 'incidencias.municipios'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name= fields.Char(string="Nombre")
    habitantes = fields.Integer(string="Habitantes")
    imagen = fields.Binary(string="Mapa del municipio")
    superficie = fields.Integer(string="Superficie")
    densidad_poblacion = fields.Float(string="Densidad Población", compute="_densidadpoblacion",store=True)
    incidencias = fields.One2many("incidencias.incidencias","municipio", string="incidencias")

    @api.depends('habitantes','superficie')
    def _densidadpoblacion(self):
        for r in self:
            if r.superficie > 0:
                r.densidad_poblacion = r.habitantes/r.superficie

class incidencias_clientes(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    incidencias = fields.One2many("incidencias.incidencias","cliente", string="incidencias")

  
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
