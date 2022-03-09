# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask_script import Manager

from app import create_app, db
from app.models import User

app = create_app("development")

manager = Manager(app)

@manager.shell
def make_shell_ctx():
    return dict(app=app, db=db, User=User)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # manager.run()
    app.run()