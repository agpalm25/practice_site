import pytest
from website import create_app
from flask import session
import os

@pytest.fixture(scope='module')
def test_client() :

    # (madi) 'set the testing configuration prior to creating the flask
    #         application'
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app = create_app()

    with app.test_client() as test_client :

        yield test_client


# @pytest.fixture(scope='module')
# def init_database(test_client):
