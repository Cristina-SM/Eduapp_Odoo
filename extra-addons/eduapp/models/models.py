# -*- coding: utf-8 -*-

from odoo import models, fields, api


class eduapp_files(models.Model):
    _name = "eduapp.files"
    _description = "eduapp.files"  
    files = fields.Binary(string="files")
    document = fields.Many2one("eduapp.resources", string = "Archivos", ondelete="cascade")



class eduapp_resources(models.Model):
    _name = "eduapp.resources"
    _description = "eduapp.resources"
    name = fields.Char(string="Nombre de los recursos")
    description = fields.Char(string="Descripcion de ese recurso")
    sessions = fields.Many2one("eduapp.session", string="Sessions", ondelete="cascade")
    document = fields.One2many("eduapp.files", "document", string = "Archivos")



class eduapp_session(models.Model):
    _name = "eduapp.session"
    _decription = "eduapp.session"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre de las clases")
    streaming = fields.Char(string="Nombre de la plataforma")
    start = fields.Datetime(string="start")
    end = fields.Datetime(string="End")
    document = fields.One2many("eduapp.resources", "sessions", string = "Recursos")

