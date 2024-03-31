from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for, make_response,
)

from authorization import AuthorizationHelper, Unauthorized
from user import user_repository
from blog import blog_repository

VULNERABLE_DOMAIN = "www.vulnerable.com:5000"
ATTACKER_DOMAIN = "www.attacker.com:5000"
POSTS = []

app = Flask(__name__, host_matching=True, static_host=VULNERABLE_DOMAIN)
app.secret_key = "impossible_to_guess"
app.config["SESSION_COOKIE_HTTPONLY"] = True


@app.context_processor
def inject_user():
    return dict(current_user=user_repository.get_user(session))


@app.route("/", host=VULNERABLE_DOMAIN)
def index():
    return render_template("index.j2", blogs=blog_repository.blogs)


@app.route("/blog/<blog_id>", methods=["GET"], host=VULNERABLE_DOMAIN)
def check_blog(blog_id):
    AuthorizationHelper.validate_session()
    selected_blog = blog_repository.get_by_id(blog_id)

    html = render_template("blog.j2", csrf_token=AuthorizationHelper.generate_token(), blog=selected_blog)
    r = make_response(html)
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return r


@app.route("/blog/<blog_id>/comment", methods=["POST"], host=VULNERABLE_DOMAIN)
def post_comment(blog_id):
    AuthorizationHelper.validate_session()
    AuthorizationHelper.validate_token()
    new_comment = request.form["comment"]
    blog_repository.post_comment_on_blog(blog_id, new_comment)
    return redirect(url_for('check_blog', blog_id=blog_id))


@app.route("/login", methods=["GET"], host=VULNERABLE_DOMAIN)
def login():
    try:
        AuthorizationHelper.validate_session()
        return redirect(url_for("index"))
    except Unauthorized:
        return render_template("login.j2")


@app.route("/profile/update-email", methods=["POST"], host=VULNERABLE_DOMAIN)
def change_email():
    AuthorizationHelper.validate_session()
    AuthorizationHelper.validate_token()

    current_user = user_repository.get_user(session)
    current_user.change_email(request.form["email"])
    return {"status": 200}


@app.route("/profile", methods=["GET"], host=VULNERABLE_DOMAIN)
def profile():
    AuthorizationHelper.validate_session()
    return render_template("profile.j2", user=user_repository.get_user(session))


@app.route("/login", methods=["POST"], host=VULNERABLE_DOMAIN)
def login_post():
    try:
        username = request.form["username"]
        password = request.form["password"]
        user = user_repository.get_by_username(username)
        assert user and user.password == password, "Invalid password"
        session["current_user"] = user.username
        return redirect(url_for("index"))
    except Exception as e:
        flash(e.args[0])
        return redirect(url_for("login"))


@app.route("/logout", host=VULNERABLE_DOMAIN)
def logout():
    session.pop("current_user")
    return redirect(url_for("index"))


# Attacker Side -> Call https://www.attacker.com:5000/leak.html to log
requests_log = []


@app.route("/leak", host=ATTACKER_DOMAIN)
def leak():
    global requests_log
    if "newmail" in request.url:
        requests_log = requests_log + [f"{request.method} {request.url}"]
    return render_template("leak.j2", requests_log=requests_log)


@app.route("/", host=ATTACKER_DOMAIN)
def evil_index():
    return redirect("leak")


@app.route("/<path:path>", host=ATTACKER_DOMAIN)
def evil_static(path):
    return send_from_directory("evil-static", path)
