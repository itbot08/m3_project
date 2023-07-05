from django.contrib.auth.models import ContentType, User, Group, Permission

class ContentType(ContentType):
    """
    ContentType
    """
    class Meta:
        proxy = True
        verbose_name = u'ContentType'
        verbose_name_plural = u'ContentType'


class User(User):
    """
    User
    """
    class Meta:
        proxy = True
        verbose_name = u'Пользователи'
        verbose_name_plural = u'Пользователи'

    is_Bool = (
        (0, u'False'),
        (1, u'True')
    )


class Group(Group):
    """
    Group
    """
    class Meta:
        proxy = True
        verbose_name = u'Группы'
        verbose_name_plural = u'Группы'

class Permission(Permission):
    """
    Permission
    """
    class Meta:
        proxy = True
        verbose_name = u'Permission'
        verbose_name_plural = u'Permission'



