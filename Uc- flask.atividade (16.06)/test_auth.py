from flask import Flask, session, redirect, url_for, request
import pytest

app = Flask(__name__)
app.secret_key = 'test_secret_key'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'testuser' and password == 'testpass':
        session['username'] = username
        return redirect(url_for('dashboard'))
    return 'Invalid credentials', 401

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Hello, {session["username"]}!'
    return redirect(url_for('login'))

def test_login(client):
    response = client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 302  # Redirect to dashboard
    assert 'username' in session

def test_logout(client):
    client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
    response = client.get('/logout')
    assert response.status_code == 302  # Redirect to index
    assert 'username' not in session

def test_invalid_login(client):
    response = client.post('/login', data={'username': 'wronguser', 'password': 'wrongpass'})
    assert response.status_code == 401  # Unauthorized

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client