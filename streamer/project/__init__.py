from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )

from .models.user import User

from .models.interpret import Interpret

import random

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(None)
    
    config.scan()
    random.seed()

    return config.make_wsgi_app()
