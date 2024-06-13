from flask import *
from .descriptions import *

bp = Blueprint('views',__name__,url_prefix='/')

@bp.route('/')
def index():
    return render_template('routes/index.html')
@bp.route('/community')
def community():
    return render_template('routes/community.html')
@bp.route('/vocational_orientation')
def vocational_orientation():
    return render_template('routes/orientation.html')
@bp.route('/presentation')
def presentation():
    return render_template('routes/presentation.html')
@bp.route('/vocational_test')
def vocational_test():
    return render_template('routes/test.html')
@bp.route('/careers')
def careers():
    return render_template('routes/careers.html',
                            informatica_concept    = informatica_concept,
                            administracion_concept = administracion_concept,
                            contabilidad_concept   = contabilidad_concept,
                            marketing_concept      = marketing_concept,
                        )
@bp.route('/contact_us')
def contact_us():
    return render_template('routes/contact.html')

###################################################
#                     CAREERS                     #
###################################################

@bp.route('/career/informatica')
def informatica():
    return render_template('routes/career_informatica.html')

@bp.route('/career/administracion')
def administracion():
    return render_template('routes/career_administracion.html')

@bp.route('/career/contabilidad')
def contabilidad():
    return render_template('routes/career_contabilidad.html')

@bp.route('/career/marketing')
def marketing():
    return render_template('routes/career_marketing.html')