from flask import Blueprint, url_for
from werkzeug.utils import redirect

from mbb.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_mbb():
    return 'Hello, mbb!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))



