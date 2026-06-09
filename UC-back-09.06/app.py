from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

COOKIE_MAX_AGE = 10 * 365 * 24 * 60 * 60  # 10 anos em segundos


def _cookie_secure_flag() -> bool:
    return not app.debug


@app.route('/')
def inicio():
    name = request.cookies.get('name')
    theme = request.cookies.get('theme', 'claro')

    return render_template(
        'inicio.html',
        name=name,
        theme=theme
    )


@app.route('/set_name', methods=['POST'])
def set_name():
    name = request.form.get('name', '').strip()

    resp = make_response(redirect(url_for('inicio')))

    if name:
        resp.set_cookie(
            'name',
            name,
            max_age=COOKIE_MAX_AGE,
            samesite='Lax',
            httponly=True,
            secure=_cookie_secure_flag()
        )
    else:
        resp.delete_cookie('name')

    return resp


@app.route('/set_theme', methods=['POST'])
def set_theme():
    theme = request.form.get('theme', 'claro')

    if theme not in ('claro', 'escuro'):
        theme = 'claro'

    resp = make_response(redirect(url_for('inicio')))

    resp.set_cookie(
        'theme',
        theme,
        max_age=COOKIE_MAX_AGE,
        samesite='Lax',
        httponly=False,
        secure=_cookie_secure_flag()
    )

    return resp


if __name__ == '__main__':
    app.run(debug=True)