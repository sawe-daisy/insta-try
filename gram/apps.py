from django.apps import AppConfig


class GramConfig(AppConfig):
    name = 'gram'

    def ready(self):
        import gram.signals
