"""
------------------------------------ Imports ------------------------------------
"""
from flask import render_template, Blueprint


"""
----------------------------------- Blueprint -----------------------------------
"""
core = Blueprint('core', __name__)


"""
------------------------------------- Views -------------------------------------
"""
@core.route('/')
def home():
   return render_template('base.html')