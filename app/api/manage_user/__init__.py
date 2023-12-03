from flask import Blueprint

user_manag_bp = Blueprint('manage_user',__name__)

from app.api.manage_user import routes