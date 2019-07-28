from flask import render_template, request, flash, url_for, redirect
from flask_login import LoginManager, login_required, login_user, UserMixin, logout_user
from project_awesome import app, db
from project_awesome.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'loginpage'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pybitesdashboard')
@login_required
def pybitesdashboard():
    return render_template('pybitesdashboard.html')

@app.route('/loginpage', methods=['GET', 'POST'])
def loginpage():
    if request.method == 'POST' and 'username' in request.form:
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user:
            if user.password == request.form.get('password'):
                login_user(user)
                return redirect(url_for('pybitesdashboard'))
        return 'Invalid username or password'

    return render_template('loginpage.html')

@app.route('/logoutpage')
@login_required
def logoutpage():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST' and 'username' in request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        add_user(username, password)
    return render_template('create_user.html')


def add_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    flash('User Created')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    pass
