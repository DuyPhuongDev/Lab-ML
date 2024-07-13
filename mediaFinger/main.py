import mediapipe as mp # type: ignore
import cv2 # type: ignore

cap = cv2.VideoCapture(1)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils

# coord laf list index
finger_coord = [(8,6), (12,10), (16,14), (20,18)]
thumb_coord = (4,2)

while True:
    success, image = cap.read()
    if not success: break
    image = cv2.flip(image, 1)
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks
    
    if multiLandMarks:
        handlist = [] # ds toa do cua landmark tren ban tay
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handlist.append((cx, cy))
        
        for point in handlist:
            cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
        upCount = 0
        
        for coordinate in finger_coord:
            if handlist[coordinate[0]][1] < handlist[coordinate[1]][1]:
                upCount += 1
        if handlist[thumb_coord[0]][0] < handlist[thumb_coord[1]][0]:
            upCount += 1
        if upCount == 5:
            upCount = 'Bao'
        elif upCount == 2:
            upCount = 'Keo'
        elif upCount == 0:
            upCount = 'Bua'
        cv2.putText(image, str(upCount), (150, 150),
                    cv2.FONT_HERSHEY_PLAIN, 12, (0, 255, 0), 12)
    cv2.imshow("Counting number of fingers", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()