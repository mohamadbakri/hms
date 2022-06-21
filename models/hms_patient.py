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
    state = fields.Selection([
        ("un", "Undetermined"),
        ("g", "Good"),
        ("f", "Fair"),
        ("s", "Serious")
    ],default="un" )
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
class PatientLog(models.Model):
    _name="hms.patient.log"

    description = fields.Text()
    patient_id = fields.Many2one("hms.patient")