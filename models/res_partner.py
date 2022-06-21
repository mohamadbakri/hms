from odoo import models, fields, api



class ResPartner(models.Model):
    _inherit = "res.partner"

    related_patient_id=fields.Many2one("hms.patient")