from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from .controller import obs
from . import models
from . import ui

class ContentTypeObjectPack(ObjectPack):
    """
    ObjectPack для модели ContentType
    """
    model = models.ContentType
    add_to_desktop = True
    add_to_menu = True

    #add_window = edit_window = ui.AddWindow
    edit_window = add_window = ModelEditWindow.fabricate(
        model, model_register=obs
    )


class UserObjectPack(ObjectPack):
    """
    ObjectPack для модели User
    """
    model = models.User
    add_to_desktop = True
    add_to_menu = True

    add_window = edit_window = ui.AddUserWindow

    columns = [
        {
            'data_index': 'id',
            'header': u'id'
        },
        {
            'data_index': 'username',
            'header': u'Логин'
        },
        {
            'data_index': 'first_name',
            'header': u'Имя'
        },
        {
            'data_index': 'last_name',
            'header': u'Фамилия'
        }]

class GroupObjectPack(ObjectPack):
    """
    ObjectPack для модели Group
    """
    model = models.Group
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(
        model, model_register=obs
    )

class PermissionObjectPack(ObjectPack):
    """
    ObjectPack для модели Permission
    """
    model = models.Permission
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(
        model, model_register=obs
    )
