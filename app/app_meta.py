from django.conf.urls import url
from objectpack import desktop
from . import actions
from . import controller


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.action_controller.urlpattern)]


def register_actions():
    """
    регистрация экшенов
    """
    controller.action_controller.packs.extend([
        actions.ContentTypeObjectPack(),
        actions.UserObjectPack(),
        actions.GroupObjectPack(),
        actions.PermissionObjectPack(),
    ])


def register_desktop_menu():
    """
    регистрация элеметов рабочего стола
    """
    desktop.uificate_the_controller(
        controller.action_controller,
        menu_root=desktop.MainMenu.SubMenu(u'Main')
    )