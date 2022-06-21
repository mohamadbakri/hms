from odoo import models, fields


class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = "Hms Patient"
    _rec_name = "first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    history = fields.Html()
    age = fields.Integer()
    birth_date = fields.Date()
    blood_type = fields.Selection([
        ("a", "A"),
        ("b", "B"),
        ("ab", "AB"),
        ("o", "O")
    ], )
    address = fields.Text()
    pcr = fields.Boolean(string="PCR")
    cr_ratio = fields.Float()
    # cr_ratio = fields.Float(attrs='{"required": [("pcr", "=", "True")]}')
    image = fields.Binary()
    department_id = fields.Many2one("hms.department")
    department_capacity = fields.Integer(related="department_id.capacity")
#     logs_ids =  fields.One2many("hms.patient.log","patient_id")
#
#
#
# class PatientLog(models.Model):
#     _name="hms.patient.log"
#
#     description = fields.Text()
#     patient_id = fields.many2one("hms.patient")