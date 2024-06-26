import cv2
import math
import keyboard

def face_capture():
    cascade_path = r'/home/user/object-recognition/haarcascade_frontalface_alt2.xml'
    
    clf = cv2.CascadeClassifier(cascade_path)
    camera = cv2.VideoCapture(0)
    x_2 = 0
    y_2 = 0
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    
        
        for (x, y, width, height) in faces:
            x_2 = x + width
            y_2 = y + height
            canter_x = int((x + x_2) / 2)
            canter_y = int((y + y_2) / 2)

            
            cv2.line(frame,  ((canter_x), 240), (320,240), (255, 255, 0), 2) # Линия для x к центру x
            cv2.line(frame,  (320,240), (320,canter_y), (255, 255, 0), 2) # Линия для y к центру y

            distances_x = math.sqrt((canter_x-320)**2 + (240-240)**2)
            distances_y = math.sqrt((320-320)**2 + (240-canter_y)**2)
            print(f" x distances is {distances_x}")
            print(f" y distances is {distances_y}")
            hypotenuse_length = math.sqrt((320 - canter_x)**2 + (240 - canter_y)**2)
            leg_length = math.sqrt((240-canter_y)**2)
            try:
                triangle_sin = leg_length/hypotenuse_length
            except ZeroDivisionError:
                triangle_sin = 0
            triangle_corner = math.degrees(math.asin(triangle_sin))
            
        
        if keyboard.is_pressed('q'):
            break
        
        
    camera.release()
    


def main():
    face_capture()
    
    
if __name__ == '__main__':
    main()

