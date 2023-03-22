import cv2
from pyzbar.pyzbar import decode

# function to validate if qr code was already scanned
def validate_qr_code(qr_code):
    # check if qr code is in the list
    if qr_code in scanned_qr_codes:
        return False
    else:
        # add qr code to the list
        scanned_qr_codes.append(qr_code)
        return True

# Create a VideoCapture object to read from the camera stream
cap = cv2.VideoCapture('http://192.168.100.254:8080/video')

while True:
    # Read a frame from the camera stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the frame
    decoded_objects = decode(gray)

    # Iterate over the decoded objects and print the decoded data
    for obj in decoded_objects:
        print(obj.data.decode())
        if validate_qr_code(obj.data.decode()):
            print('QR Code Scanned')
            break

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and destroy the windows
cap.release()
cv2.destroyAllWindows()
