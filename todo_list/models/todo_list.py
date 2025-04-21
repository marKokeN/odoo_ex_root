from odoo import models, fields

class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'

    name = fields.Char(string="Tag", required=True)

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string="Test Titile", required=True)
    tag_ids = fields.Many2many('todo.tag', string="Tags")
