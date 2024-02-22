import cv2
import math


def face_capture():
    cascade_path = r'C:\Users\user\Desktop\object-recognition\haarcascade_frontalface_alt2.xml'
    
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
            cv2.rectangle(frame, (x, y), (x_2, y_2), (255, 255, 0), 2)
            cv2.circle(frame, (320,240),  2, (255, 255, 0), 2)
            canter_x = int((x + x_2) / 2)
            canter_y = int((y + y_2) / 2)

            cv2.line(frame, (320,240), (canter_x, canter_y), (255, 255, 0), 2)


            hypotenuse_length = math.sqrt((320 - canter_x)**2 + (240 - canter_y)**2)
            leg_length = math.sqrt((240-canter_y)**2)
            try:
                triangle_sin = leg_length/hypotenuse_length
            except ZeroDivisionError:
                triangle_sin = 0
            triangle_corner = math.degrees(math.asin(triangle_sin))
            print(triangle_corner)
        cv2.imshow('Faces', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        
        
    camera.release()
    cv2.destroyAllWindows()


def main():
    face_capture()
    
    
if __name__ == '__main__':
    main()
