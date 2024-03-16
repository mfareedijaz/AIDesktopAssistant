import cv2
import mediapipe as mp
import pyautogui

def mouse():
    x1 = y1 = x2 = y2 = 0
    webcam = cv2.VideoCapture(0)
    my_hands = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_y = 0
    while True:
        _ , image = webcam.read()
        image = cv2.flip(image,1)
        frame_height, frame_width, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output = my_hands.process(rgb_image)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(image, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=image, center=(x,y), radius=8, color=(0,255,255), thickness=3)
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                        pyautogui.moveTo(index_x, index_y)
                        x1 = x
                        y1 = y 
                    if id == 4:
                        x2 = x
                        y2 = y
                        cv2.circle(img=image, center=(x,y), radius=8, color=(0,0,255), thickness=3)
                        # thumb_x = screen_width/frame_width*x
                        # thumb_y = screen_height/frame_height*y
                        # if abs(index_y-thumb_y) < 10:
                        #     pyautogui.click()
                        #     pyautogui.sleep(1)
            dist = y2 - y1
            if(dist<20):
                pyautogui.click()                
        cv2.imshow("Virtual Mouse", image)
        key = cv2.waitKey(100)
        if key == 27:
            break
    webcam.release()
    cv2.destroyAllWindows()
    # return "Volume changed successfully"