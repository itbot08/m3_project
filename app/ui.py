# -*- coding: utf-8 -*-
from objectpack.ui import ModelEditWindow, BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from . import models

class AddUserWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна
        """
        super(AddUserWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            format='d.m.Y',
            label=u'last login',
            name='last_login',
            allow_blank=False,
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            allow_blank=False,
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            allow_blank=False,
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'active',
            name='is_active',
            allow_blank=False,
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            format='d.m.Y',
            label=u'date joined',
            name='date_joined',
            allow_blank=False,
            anchor='100%'
            )

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')


    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(AddUserWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна
        """
        super(AddUserWindow, self).set_params(params)
        self.height = 'auto'