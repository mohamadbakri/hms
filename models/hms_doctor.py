from odoo import models, fields


class HmsDoctor(models.Model):
    _name = "hms.doctor"
    _description = "Hms Doctors"
    _rec_name = "full_name"

    full_name = fields.Char(compute="get_full_name")
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    image = fields.Binary()

    def get_full_name(self):
        for rec in self:
            self.full_name=f"{rec.first_name} {rec.last_name}"