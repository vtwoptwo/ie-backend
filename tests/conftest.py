import pytest
from backend_api.models import Recipe
from backend_api import db, app 
from backend_api.routes import *


@pytest.fixture
def testing_client(scope='module'):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.add(Recipe(name='soup', ingredients='water', instructions='boil', favorite=False, rating=4))
            db.session.commit()
            yield client
            yield testing_client
            db.drop_all()

import pytest