from flask import Flask, Response
import cv2

app = Flask(__name__)

# Initialize the camera (use 0 for the default camera)
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Use a generator to stream the frame in multipart format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Route to display video stream
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # Run the Flask app on all available IPs on port 5000
    app.run(host='0.0.0.0', port=5000)
