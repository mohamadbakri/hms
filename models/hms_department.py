from odoo import models, fields


class HmsDepartment(models.Model):
    _name = "hms.department"
    _description = "Hms Department"
    _rec_name = "name"

    name = fields.Char(requierd=True)
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_ids = fields.One2many("hms.patient", "department_id")
