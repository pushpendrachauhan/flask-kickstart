from flask import Blueprint,request

mod_a_bp = Blueprint('user', __name__, url_prefix='/kickstart')

@mod_a_bp.route('/v1/users/', methods=('GET', 'POST'))
def register():
	if request.method == 'GET':
		return "push"
