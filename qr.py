import streamlit as st
import pyqrcode
import cv2

def scan_qr():
    st.write("Scanning QR Code...")
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data, _, _ = detector.detectAndDecode(img)
        if data:
            cap.release()
            cv2.destroyAllWindows()
            st.write("QR Code Scanned:", data)
            return data
        st.image(img, channels="BGR", use_column_width=True)
        if cv2.waitKey(1) == 113:  # ASCII value of 'q'
            break

def generate_qr(text):
    if len(text) != 0:
        qr = pyqrcode.create(text)
        st.image(qr.xbm(scale=8), channels="L", use_column_width=True)
        st.write("Generated QR Code for:", text)
    else:
        st.warning('All Fields are Required!')

def main():
    st.title('QR code Generator & Scanner')

    action = st.radio("Choose Action", ["Generate QR Code", "Scan QR Code"])

    if action == "Generate QR Code":
        user_input = st.text_input("Enter message or URL")
        generate_qr(user_input)
    elif action == "Scan QR Code":
        scan_qr()

if __name__ == "__main__":
    main()
