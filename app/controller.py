from objectpack import observer

# Наблюдатель
obs = observer.Observer()

action_controller = observer.ObservableController(obs, "/controller")

@obs.subscribe
class Listener(object):

    listen = ['.*/.*/ObjectListWindowAction']

    def after(self, request, context, response):
        # подмена заголовка окна
        pass
        # response.data.title = u'Му-ха-ха! %s' % response.data.title

@obs.subscribe
class StarToHash(object):

    listen = ['.*/BandedColumnPack/.*']

    def prepare_obj(self, obj):
        obj['field1'] = obj.get('field1', False) and (obj['id'] % 2)
        return obj