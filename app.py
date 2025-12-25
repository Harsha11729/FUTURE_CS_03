from flask import Flask, render_template, request, send_file
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
KEY_FILE = "secret.key"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load AES key
with open(KEY_FILE, "rb") as f:
    SECRET_KEY = f.read()

def encrypt_file(data):
    iv = get_random_bytes(16)
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)

    # Padding
    pad_len = 16 - len(data) % 16
    data += bytes([pad_len]) * pad_len

    encrypted_data = cipher.encrypt(data)
    return iv + encrypted_data

def decrypt_file(data):
    iv = data[:16]
    encrypted_data = data[16:]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)

    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove padding
    pad_len = decrypted_data[-1]
    return decrypted_data[:-pad_len]

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename == "":
            return "No file selected"

        data = file.read()
        encrypted_data = encrypt_file(data)

        encrypted_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename + ".enc"
        )

        with open(encrypted_path, "wb") as f:
            f.write(encrypted_data)

        return f"File '{file.filename}' encrypted and stored securely!"

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    encrypted_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename + ".enc"
    )

    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data)

    decrypted_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    with open(decrypted_path, "wb") as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

