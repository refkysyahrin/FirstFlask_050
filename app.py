from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Data pengguna (dummy)
users = {
    "admin": "admin123",
    "user": "userpass"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            flash("Login berhasil!", "success")
            return redirect(url_for('index'))  # Redirect ke formulir mahasiswa
        else:
            flash("Username atau password salah.", "error")
            return render_template('login.html')

    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        program_studi = request.form['program_studi']
        alamat = request.form['alamat']
        nomor_telepon = request.form['nomor_telepon']
        email = request.form['email']
        
        return render_template('halamandata.html', nim=nim, nama=nama, 
                               tempat_lahir=tempat_lahir, tanggal_lahir=tanggal_lahir, 
                               program_studi=program_studi, alamat=alamat, 
                               nomor_telepon=nomor_telepon, email=email)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
