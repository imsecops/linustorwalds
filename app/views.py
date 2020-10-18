from app import app
from flask import abort, render_template, request, redirect, url_for, send_from_directory


###
### General
###
@app.route('/recover_password', subdomain="<subdomain>", methods=['GET', 'POST'])
def recover_password(subdomain):
    if request.method == 'GET':
        return render_template('_restore.html')

@app.route('/robots.txt', subdomain="<subdomain>", methods=['GET', 'POST'])
def robots_txt(subdomain):
    if request.method == 'GET':
        return send_from_directory(app.static_folder, "robots.txt")

# ###
# ### Level 3: Linus we love you!
# ###
@app.route('/', subdomain="linustorwalds", methods=['GET', 'POST'])
def level3():
    if request.method == 'GET':
        is_invalid = request.args.get("is_invalid", default="0") in ["true", "1"]
        return render_template('level3.html', level="3", hint="Linus we love you!", is_invalid=is_invalid)
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '8GmX@pPxt@E&F':
            return redirect(url_for('level4'))
        else:
            return render_template('level3.html', level="3", hint="Linus we love you!", is_invalid=True)