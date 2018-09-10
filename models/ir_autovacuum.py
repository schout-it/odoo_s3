# -*- coding: utf-8 -*-

from odoo import api, models
from odoo import SUPERUSER_ID


def copy_filestore_to_s3(cr, registry, module):
    ''' This is a utility function used to preserve existing previous tags during upgrade of the module.'''
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.attachment']._copy_filestore_to_s3()


class AutoVacuum(models.AbstractModel):
    _inherit = 'ir.autovacuum'

    @api.model
    def power_on(self, *args, **kwargs):
        self.env['ir.attachment']._copy_filestore_to_s3()
        self.env['ir.attachment']._file_gc_s3()
        return super(AutoVacuum, self).power_on(*args, **kwargs)

