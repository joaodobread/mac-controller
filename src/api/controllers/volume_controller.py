from flask import Blueprint, render_template, redirect, url_for, request
import osascript

volume_controller = Blueprint(
    'volume_controller', __name__, url_prefix='/volume')


@volume_controller.route('/', methods=['GET'])
def index():
    code, out, err = osascript.run("output volume of (get volume settings)")
    if err:
        render_template('error.html', err)
    return render_template('volume/index.html', volume=out)


@volume_controller.route('/update', methods=['POST'])
def update_volume():
    new_volume = request.form.get('volume')
    code, out, err = osascript.run(f"set volume output volume {new_volume}")
    if err:
        render_template('error.html', err)
    return redirect(url_for('volume_controller.index'))
