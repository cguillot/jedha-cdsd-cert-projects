# Module de pilotage du Robot avec 5 threads :
# - navig_thread
#   Pilotage des moteurs en fonction de :
#   - des indications infrarouge de suivi de ligne sur la route
#   - des panneaux de limitations détectés
#
# - capture_thread
#   Détection des panneaux
#
# - digits_thread
#   Affichage des panneaux détéctés sur l'afficheur du robot
#
# - ultras_thread
#   Détection de distance d'objet devant le robot
#
# - http_thread
#   Serveur http de diffusion des images vue par le robot
#
#
#
import threading
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from picamera2 import Picamera2
import cv2
from model_3 import warm as cnn_warm, predict as ncnn_predict
import numpy as np
from Motor import *
import RPi.GPIO as GPIO
import tm1637
from ultras import *


# Global variable
frame = None
signs_detected = []
ultras_dist = None


classNames = ['Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110', 'Speed Limit 120', 'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40', 'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70', 'Speed Limit 80', 'Speed Limit 90', 'Stop']
classDigitDispaly = ["PASS","HALT", 10, 100, 110, 120, 20, 30, 40, 50, 60, 70, 80, 90, "STOP"]
classRobotMove = [True, False, True, True, True, True, True, True, True, True, True, True, True, True, False]
classRobotSpeed = [None, None, .6, 1.5, 1.6, 1.7, .7, .8, .9, 1., 1.1, 1.2, 1.3, 1.4, None]


# Class à prendre en compte pour la démo Robot.
classDemo = [4, 7, 9, 13, 14]


def ultras_detect() :
    global ultras_dist

    while True :
        ultras_dist = ultrasonic.get_distance()
        time.sleep(.5)


def display_digit() :

    global signs_detected

    tm = tm1637.TM1637(clk=21, dio=20)
    tm.write([0, 0, 0, 0])
    tm.show("JDHA")

    current_display_class = -1

    while True :

        detected = signs_detected

        if len(detected) != 0 :
            posConfMax = np.argmax(np.array([det["cls"] for det in detected]))
            display_class = detected[posConfMax]["cls"]

            if display_class != current_display_class :
                display = classDigitDispaly[display_class]
                if isinstance(display, int) :
                    tm.number(display)
                else :
                    tm.show(display)
                current_display_class = display_class

        time.sleep(.1)


def navigation():

    global signs_detected
    global ultras_dist

    IR01 = 14
    IR02 = 15
    IR03 = 23

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR01,GPIO.IN)
    GPIO.setup(IR02,GPIO.IN)
    GPIO.setup(IR03,GPIO.IN)

    r_speed = 1
    r_move = False
    ultras_dist_limit = 10

    while True :

        detected = signs_detected

        if len(detected) != 0 :
            posConfMax = np.argmax(np.array([det["cls"] for det in detected]))
            classConfMax = detected[posConfMax]["cls"]

            if classRobotSpeed[classConfMax] != None :
                r_speed = classRobotSpeed[classConfMax]
            r_move = classRobotMove[classConfMax]

        if ultras_dist != None :
            if ultras_dist < ultras_dist_limit :
                r_move = False


        if r_move :
            c_speed = r_speed
        else :
            c_speed = 0


        ns = int(650 * c_speed)
        rs1f = int(2000 * 1)
        rs1b = -int(1000 * 1)
        rs2f = int(1500 * 1)
        rs2b = -int(750 * 1)


        LMR=0x00
        if GPIO.input(IR01) == True:
            LMR = (LMR | 4)
        if GPIO.input(IR02) == True:
            LMR = (LMR | 2)
        if GPIO.input(IR03) == True:
            LMR = (LMR | 1)
        if LMR == 2:
            PWM.setMotorModel(ns, ns, ns, ns)
        elif LMR == 4:
            PWM.setMotorModel(rs2b, rs2b, rs2f, rs2f)
        elif LMR == 6:
            PWM.setMotorModel(rs1b, rs1b, rs1f, rs1f)
        elif LMR==1:
            PWM.setMotorModel(rs2f, rs2f, rs2b, rs2b)
        elif LMR==3:
            PWM.setMotorModel(rs1f, rs1f, rs1b, rs1b)
        elif LMR==7:
            #pass
            PWM.setMotorModel(0, 0, 0, 0)


def capture_frames(save_stream=False):
    """
    Captures frames from Picamera2 and updates the global frame variable.
    """
    global signs_detected
    global frame


    camera = Picamera2()

    # ChatGPT
    # camera_config = camera.create_still_configuration(main={"size": (640, 480)})

    # Seddik
    #picam2.set_controls({"ExposureTime": 10000})  # Ajuster le temps d'exposition )
    camera_config = camera.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"})
    # camera_config = camera.create_preview_configuration(main={"size": (640, 480)})
    fps = 15.0
    camera.controls.FrameRate = fps

    camera.configure(camera_config)
    camera.start()

    video_writer = None

    if save_stream:
      # save_dir = os.getenv('DSFS_FT_31_SAVE_BASE_DIR', '/app/dump')
      save_dir = '.'
      output_video_filename = f"inference_stream_{time.strftime('%Y%m%d_%H%M%S')}.avi"

      # Define the directory containing your images relative to the script location
      output_video_path = os.path.join(save_dir, output_video_filename)

      print(f"Generated filename: {output_video_path}")
      fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use 'XVID' or 'MJPG' for .avi files
      video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (640, 480))


    try:
        while True:
            # raw_frame = np.array(camera.capture_buffer()).reshape(480, 640, 3)

            raw_frame = camera.capture_array()
            predicted = ncnn_predict(raw_frame)
            frame = predicted['image']
            detected = predicted['detected']

            signs_detected = [det for det in detected if det["cls"] in classDemo]

            if video_writer:
              video_writer.write(frame)

            # time.sleep(0.33)  # 30 FPS
            # time.sleep(0.33)  # 30 FPS


    finally:
        camera.stop()

class StreamingHandler(BaseHTTPRequestHandler):
    """
    HTTP handler to serve a basic index page and stream MJPEG frames.
    """
    def do_GET(self):
        if self.path == '/':
            # Serve a simple HTML page with a video element
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Camera Stream</title>
                </head>
                <body>
                    <h1>JEDHA - Data Science Fullstack - DemoDay</h1>
                    <p>Live stream</p>
                    <img src="/rpi-eye" />
                </body>
                </html>
            """)
        elif self.path == '/rpi-eye':
            # Serve the MJPEG stream
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            while True:
                if frame is not None:
                    ret, jpeg = cv2.imencode('.jpg', frame)
                    if ret:
                        self.wfile.write(b'--frame\r\n')
                        self.wfile.write(b'Content-Type: image/jpeg\r\n\r\n')
                        self.wfile.write(jpeg.tobytes())
                        self.wfile.write(b'\r\n')
                    time.sleep(0.033)  # Adjust as needed for your desired FPS
        else:
            # Handle unknown paths with a 404 error
            self.send_error(404)
            self.end_headers()

def start_http_server():
    """
    Starts the HTTP server.
    """
    server = HTTPServer(('0.0.0.0', 5000), StreamingHandler)
    server.serve_forever()



if __name__ == "__main__":

    ## save_stream = os.getenv('DSFS_FT_31_SAVE_STREAM', 'false') == 'true'
    save_stream = True
    if save_stream:
      print('Inference stream will be saved')

    cnn_warm()
    # Create threads
    navig_thread = threading.Thread(target=navigation, daemon=True)
    capture_thread = threading.Thread(target=capture_frames, args=(save_stream,), daemon=True)
    digits_thread = threading.Thread(target=display_digit, daemon=True)
    ultras_thread = threading.Thread(target=ultras_detect, daemon=True)
    http_thread = threading.Thread(target=start_http_server, daemon=True)

    # Start threads
    navig_thread.start()
    capture_thread.start()
    digits_thread.start()
    ultras_thread.start()
    http_thread.start()


    # Keep the main thread alive
    navig_thread.join()
    capture_thread.join()
    digits_thread.join()
    ultras_thread.join()
    http_thread.join()

