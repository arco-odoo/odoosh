# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SpaceShip(models.Model):
    
    _name = 'space_mission.space_ship'
    _description = 'Space ship details'
    
    name = fields.Char(title='Name')
    height = fields.Integer(string='Height')
    width = fields.Integer(string='Width')
    