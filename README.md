# 🔐 QR Code Authenticity Detection System

## 📌 Project Overview

This project is a **QR Code Security System** that detects whether a scanned QR code is **REAL (trusted)** or **FAKE (fraudulent)**.

It simulates a real-world situation where:

* A customer scans a QR code in a shop
* The system checks if it is genuine or tampered
* If real → proceeds to payment + OTP
* If fake → shows warning and blocks transaction

---

## 🎯 Objectives

* Detect fake QR codes used in scams
* Simulate secure digital payment verification
* Prevent fraud in QR-based payments
* Provide visual scanning simulation

---

## ⚙️ Features

* ✅ Random QR generation (Real + Fake)
* ✅ QR scanning using OpenCV
* ✅ Animated scanning process
* ✅ Merchant authenticity verification
* ✅ OTP generation for real QR
* ✅ Fake QR detection warning
* ✅ Clean UI display (no auto close)

---

## 🧠 Working Principle

1. The system generates a QR code randomly
2. QR contains merchant information
3. System scans the QR code
4. Extracts merchant data
5. Compares with trusted database
6. Displays result:

| QR Type | Output                   |
| ------- | ------------------------ |
| REAL QR | Proceed to Payment + OTP |
| FAKE QR | Warning: Fake QR         |

---

## 🛠️ Technologies Used

* Python
* OpenCV (`cv2`)
* PyOTP
* QRCode Library
* NumPy

---

## 💻 Installation

### Step 1: Install Python

Download from:
https://www.python.org/downloads/

✔ Make sure to check **"Add Python to PATH"**

---

### Step 2: Install Required Libraries

Open terminal in VS Code and run:

```bash
python -m pip install opencv-python pyotp qrcode pillow numpy
```

---

## ▶️ How to Run the Project

1. Open project folder in VS Code
2. Run the file:

```bash
python qr_payment_system.py
```

---

## 📂 Project Structure

```
qr_project/
│
├── qr_payment_system.py   # Main program file
├── random_qr.png         # Generated QR image
└── README.md             # Documentation
```

---

## 🧪 Output

* QR code is displayed
* Scanning animation runs
* Result shown on screen:

✔ REAL → "Proceed to Payment" + OTP
❌ FAKE → "Fake QR Detected"

---

## 🚀 Future Enhancements

* Database integration (SQLite/MySQL)
* Mobile app version
* Real payment gateway integration
* AI-based QR fraud detection
* GUI interface (Tkinter)

---

## 🧠 Viva Explanation

"This system verifies QR code authenticity by extracting merchant data embedded inside the QR and comparing it with a trusted database. If the QR belongs to a registered merchant, the system allows payment and generates OTP. Otherwise, it detects it as a fake QR and blocks the transaction."

---

## 👨‍💻 Author

Name: Sriman G
Project: QR Code Authenticity Detection System

---

## 📜 License

This project is developed for educational purposes only.
