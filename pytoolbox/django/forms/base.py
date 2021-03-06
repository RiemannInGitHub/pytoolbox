# -*- encoding: utf-8 -*-

"""
Extra forms.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from django.utils.functional import cached_property

from ..models import utils as _utils
from ... import module

_all = module.All(globals())


class SerializedInstanceForm(object):

    def __init__(self, **kwargs):
        self.app_label = kwargs['app_label']
        self.model = kwargs['model']
        self.pk = kwargs['pk']

    @classmethod
    def serialize(cls, instance):
        return _utils.get_content_type_dict(instance)

    @cached_property
    def instance(self):
        return _utils.get_instance(self.app_label, self.model, self.pk)

    def is_valid(self):
        try:
            return bool(self.instance)
        except:
            return False

_all = module.All(globals())
