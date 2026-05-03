import cv2
import pyotp
import qrcode
import numpy as np
import random
from urllib.parse import urlparse, parse_qs, unquote

# -------------------------------
# TRUSTED MERCHANT DATABASE
# -------------------------------
trusted_merchants = ["shop@payment.com"]

# -------------------------------
# GENERATE QR
# -------------------------------
def generate_qr(data, filename):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# -------------------------------
# VALIDATION FUNCTION
# -------------------------------
def check_qr_real_or_fake(data):
    parsed = urlparse(data)
    params = parse_qs(parsed.query)

    issuer = params.get("issuer", [""])[0]

    path = parsed.path

    if ":" in path:
        merchant = path.split(":")[1]
    else:
        merchant = ""

    merchant = unquote(merchant)

    if merchant not in trusted_merchants:
        return False, merchant

    if issuer != "MyApp":
        return False, merchant

    return True, merchant

# -------------------------------
# SCAN FUNCTION
# -------------------------------
def scan_qr(file_path):
    img = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()

    print("\nScanning", file_path, "...")

    h, w = img.shape[:2]

    for i in range(0, h, 8):
        frame = img.copy()
        cv2.line(frame, (0, i), (w, i), (0, 255, 0), 2)
        cv2.putText(frame, "Scanning QR...", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.imshow("Scanner", frame)
        cv2.waitKey(15)

    data, bbox, _ = detector.detectAndDecode(img)

    return data if data else None

# -------------------------------
# DISPLAY RESULT
# -------------------------------
def show_screen(file_path, title, text, color=(0,255,0)):
    img = cv2.imread(file_path)
    h, w = img.shape[:2]

    canvas = 255 * np.ones((h + 80, w, 3), dtype="uint8")
    canvas[0:h, 0:w] = img

    cv2.putText(canvas, text, (20, h + 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow(title, canvas)
    cv2.waitKey(2000)

# -------------------------------
# RANDOM QR GENERATION
# -------------------------------
print("\n--- GENERATING RANDOM QR ---")

is_real_qr = random.choice([True, False])

if is_real_qr:
    print("Generated: REAL QR")

    secret = pyotp.random_base32()
    uri = pyotp.TOTP(secret).provisioning_uri(
        name="shop@payment.com",
        issuer_name="MyApp"
    )

else:
    print("Generated: FAKE QR")

    secret = pyotp.random_base32()
    uri = pyotp.TOTP(secret).provisioning_uri(
        name="fraud@scam.com",
        issuer_name="FakeApp"
    )

generate_qr(uri, "random_qr.png")

# -------------------------------
# SCAN QR
# -------------------------------
data = scan_qr("random_qr.png")

if data:
    is_real, merchant = check_qr_real_or_fake(data)

    if is_real:
        print("Result: REAL QR")
        show_screen("random_qr.png", "PAYMENT", "Proceed to Payment", (0,255,0))
    else:
        print("Result: FAKE QR")
        show_screen("random_qr.png", "WARNING", "Fake QR", (0,0,255))

cv2.destroyAllWindows()
