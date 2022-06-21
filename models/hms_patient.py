from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

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
    email = fields.Char()
    state = fields.Selection([
        ("un", "Undetermined"),
        ("g", "Good"),
        ("f", "Fair"),
        ("s", "Serious")
    ],default="un" )
    doctors_ids=fields.Many2many("hms.doctor")
    department_id = fields.Many2one("hms.department")
    department_capacity = fields.Integer(related="department_id.capacity")
    logs_ids =  fields.One2many("hms.patient.log","patient_id")
    def set_good(self):
        self.state="g"
        self._add_log("Good")

    def set_fair(self):
        self.state="f"
        self._add_log("Fair")

    def set_serious(self):
        self.state="s"
        self._add_log("Serious")

    def _add_log(self, state):
        self.env["hms.patient.log"].create({
            "description": f"State changed to {state}",
            "patient_id":self.id
        })

    @api.onchange('age')
    def _onchange_state(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'domain': {},
                'warning': {'title': "warning",
                           'message': "PCR field has been checked"}
                   }

    @api.constrains("email")
    def _validate_email(self):
        pattern = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        if not re.fullmatch(pattern, self.email):
            raise ValidationError("Email is not valid")

    _sql_constraints = [
        ('unique_email', 'UNIQUE(email)', 'Email already exists')
    ]


class PatientLog(models.Model):
    _name="hms.patient.log"

    description = fields.Text()
    patient_id = fields.Many2one("hms.patient")