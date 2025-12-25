# FUTURE_CS_03Secure File Sharing System
📌 Project Overview

This project is a Secure File Sharing System developed as part of Cyber Security Task 3 – Future Interns.
The application allows users to upload and download files securely by encrypting files using AES (Advanced Encryption Standard) before storing them on the server.

The main goal of this project is to demonstrate secure file handling, basic cryptography, and secure application development practices.

🎯 Features

Secure file upload functionality

AES-256 encryption for files at rest

Secure file download with decryption

Random Initialization Vector (IV) for each file

Simple and clean user interface

Basic encryption key management

Plaintext files are never stored on disk

🛠️ Technologies Used

Python

Flask – Web framework

PyCryptodome – AES encryption library

HTML & CSS – Frontend

Git & GitHub – Version control

📁 Project Structure
secure_file_sharing/
│
├── app.py                  # Flask application
├── generate_key.py         # AES key generator
├── secret.key              # Encryption key (ignored in GitHub)
├── uploads/                # Encrypted files storage
├── templates/
│   └── index.html          # Frontend UI
├── README.md               # Project documentation
└── .gitignore              # Ignored files

🔐 Encryption Details

Algorithm: AES (Advanced Encryption Standard)

Key Size: 256-bit

Mode: CBC (Cipher Block Chaining)

IV: Randomly generated for each file

Files are encrypted before storage and decrypted only when downloaded.

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/secure-file-sharing.git
cd secure-file-sharing

2️⃣ Install Dependencies
pip install flask pycryptodome

3️⃣ Generate AES Key (Run Once)
python generate_key.py

4️⃣ Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000

🧪 How It Works
🔹 File Upload

User selects a file from the browser

File is encrypted using AES-256

Encrypted file (.enc) is stored on the server

🔹 File Download

Encrypted file is read from storage

File is decrypted using the AES key

Original file is returned to the user

🔑 Key Management

AES key is generated once using a secure random generator

Key is stored locally in secret.key

Key file is excluded from GitHub using .gitignore

This represents basic key management, suitable for a demo-level secure system.

⚠️ Limitations

No user authentication or authorization

Encryption key is stored locally

Decrypted files are temporarily written to disk during download

These limitations are acceptable for learning purposes but should be improved in production systems.

📽️ Walkthrough Video

A short walkthrough video is provided demonstrating:

File upload

Encryption in action

Secure download process

Code explanation

🧠 Learning Outcomes

Understanding AES encryption

Secure file storage concepts

Flask web development basics

Key management fundamentals

Secure coding practices

📝 Conclusion

This project demonstrates a simple yet effective approach to secure file sharing using AES encryption. It highlights the importance of encrypting sensitive data at rest and provides a strong foundation for building more advanced secure applications.

👤 Author

Harsha Kandepu
Cyber Security Intern – Future Interns

📜 License

This project is developed for educational and internship purposes only.
