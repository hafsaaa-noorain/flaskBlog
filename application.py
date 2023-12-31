import socket

from helpers import (
    secrets,
    message,
    render_template,
    getProfilePicture,
    Flask,
)

from routes.post import postBlueprint
from routes.user import userBlueprint
from routes.index import indexBlueprint
from routes.login import loginBlueprint
from routes.signup import signUpBlueprint
from routes.logout import logoutBlueprint
from routes.search import searchBlueprint
from routes.editPost import editPostBlueprint
from routes.searchBar import searchBarBlueprint
from routes.dashboard import dashboardBlueprint
from routes.verifyUser import verifyUserBlueprint
from routes.adminPanel import adminPanelBlueprint
from routes.createPost import createPostBlueprint
from routes.setUserRole import setUserRoleBlueprint
from routes.passwordReset import passwordResetBlueprint
from routes.changeUserName import changeUserNameBlueprint
from routes.changePassword import changePasswordBlueprint
from routes.adminPanelUsers import adminPanelUsersBlueprint
from routes.adminPanelPosts import adminPanelPostsBlueprint
from routes.accountSettings import accountSettingsBlueprint
from routes.adminPanelComments import adminPanelCommentsBlueprint
from routes.changeProfilePicture import changeProfilePictureBlueprint
from dbChecker import dbFolder, usersTable, postsTable, commentsTable
from flask_wtf.csrf import CSRFProtect, CSRFError

dbFolder()
usersTable()
postsTable()
commentsTable()

application = Flask(__name__)
application.secret_key = secrets.token_urlsafe(32)
application.config["SESSION_PERMANENT"] = True
csrf = CSRFProtect(application)


@application.context_processor
def utility_processor():
    getProfilePicture
    return dict(getProfilePicture=getProfilePicture)


@application.errorhandler(404)
def notFound(e):
    message("1", "404")
    return render_template("404.html"), 404


@application.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template("csrfError.html", reason=e.description), 400


application.register_blueprint(postBlueprint)
application.register_blueprint(userBlueprint)
application.register_blueprint(indexBlueprint)
application.register_blueprint(loginBlueprint)
application.register_blueprint(signUpBlueprint)
application.register_blueprint(logoutBlueprint)
application.register_blueprint(searchBlueprint)
application.register_blueprint(editPostBlueprint)
application.register_blueprint(dashboardBlueprint)
application.register_blueprint(searchBarBlueprint)
application.register_blueprint(adminPanelBlueprint)
application.register_blueprint(createPostBlueprint)
application.register_blueprint(verifyUserBlueprint)
application.register_blueprint(setUserRoleBlueprint)
application.register_blueprint(passwordResetBlueprint)
application.register_blueprint(changeUserNameBlueprint)
application.register_blueprint(changePasswordBlueprint)
application.register_blueprint(adminPanelUsersBlueprint)
application.register_blueprint(adminPanelPostsBlueprint)
application.register_blueprint(accountSettingsBlueprint)
application.register_blueprint(adminPanelCommentsBlueprint)
application.register_blueprint(changeProfilePictureBlueprint)

match __name__:
    case "__main__":
        application.run(debug=True, host=socket.gethostbyname(socket.gethostname()))
