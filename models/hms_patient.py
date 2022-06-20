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
    image = fields.Binary()
    department_id = fields.Many2one("hms.department")
