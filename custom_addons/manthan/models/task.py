from datetime import time

from odoo import api, fields, models


# class Students(models.Model):
#     # _inherit = 'student.student'





class task(models.Model):
    _name = 'tasks.tasks'
    _description = 'task description'
    _rec_name = 'task_name'

    task_technology = fields.Char(string='Task Technology Used')
    student_id = fields.Many2one('student.student',string='Student')
    task_name = fields.Char(string='Task Name')
    #task_technology = fields.Char(string='Task Technology Used')
    # task_done = fields.Boolean()
    # task_not_done = fields.Boolean()
    # task_start_time = fields.Datetime(string='Task Start Date', required=False)
    # task_end_time = fields.Datetime(string='Task end Date', required=False
    #                                 )
    # company_name = fields.Char("Company Name", placeholder="enter the comapny name")
