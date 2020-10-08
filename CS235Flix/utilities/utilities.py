from flask import Blueprint, request, render_template, redirect, url_for, session

import CS235Flix.repositorydir.repository as repo
import CS235Flix.utilities.services as services

# configure Blueprint
utilities_blueprint = Blueprint('utilities_bp', __name__)


def get_genres_and_urls():
    pass
