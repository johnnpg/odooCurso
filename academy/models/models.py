# -*- coding: utf-8 -*-

from odoo import models, fields, api

class academy(models.Model):
    _name = 'academy.academy'

    name = fields.Char("Nombre")
    active = fields.Boolean()
    students = fields.Integer()
    budget = fields.Float("Presupuesto")
    history = fields.Text("Historia")
    career = fields.Selection([('ing',"ingenieria en sistema"),("med","medicina")])

    website = fields.Html("Website")
    start_date =fields.Date("Fundaa")
    open_time = fields.Datetime("Hora de apertura")
    Course_ids = fields.One2many("course","academy_id")

class course(models.Model):
    _name = "course"

    academy_id = fields.Many2one("academy.academy")
    name = fields.Char("Nombre")
    start = fields.Date("Inicio")
    end =fields.Datetime("Finaliza")
    professor_ids = fields.Many2one("profesor")
    student_ids = fields.One2many("student","course_id")


class professor(models.Model):
    _name ="profesor"

    name = fields.Char("profesor")
    career_ids = fields.Many2many("career")

class student(models.Model):
      _name = "student"

      name = fields.Char("estudiante")
      course_id = fields.Many2one("course")


class Career(models.Model):
    _name = "career"

    name = fields.Char("Nombre")


    # @api.depends("name","lasname")
    # @api.one
    # def _get_name_full(self):
    #     if self.name  and self.lasname:
    #        self.full_name = self.name +" "+ self.lasname
    #
    # name = fields.Char(string="Primer Nombre",  help ="Escriba su primer nombre", readonly=False, requiered=True , index=True,
    #                    Default="" )
    #
    # lasname = fields.Char(String="Apellido")
    #
    # full_name = fields.Char(compute="_get_name_full")

    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100