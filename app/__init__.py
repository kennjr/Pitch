import config
from flask import Flask

app = Flask(__name__)

from app.main import views, errors

# db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# We prefix the login endpoint with the blueprint name because it is located inside a blueprint.
# login_manager.login_view = 'auth.login'
# bootstrap = Bootstrap()

# photos = UploadSet('photos', IMAGES)
def create_app(config_name):

    # Creating the app configurations
    app.config.from_object(config.config_options[config_name])
    # configure UploadSet
    # configure_uploads(app, photos)
    # Will add the views and forms
    # Registering the blueprint
    # bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    # db.init_app(app)
    # login_manager.init_app(app)

    return app

