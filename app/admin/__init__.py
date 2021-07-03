from flask import Blueprint


admin = Blueprint('admin', __name__)

from .views.subject_group import *
from .views.staff import *
from .views.organisation import *
from .views.signup import *
from .views.project import *
from .views.site import *
from .views.node import *

