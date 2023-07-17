import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

#调用要使用的模型
mpHands = mp.solutions.hands #处理手部的模型
mpDraw = mp.solutions.drawing_utils #绘制模型

#设置使用模型的具体的参数
hands = mpHands.Hands() #设置处理手部模型参数
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=5)  #设置绘制点模型的参数
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=3)  #设置绘制线模型的参数

while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #把RGB图片交给设置好的模型处理
        result = hands.process(imgRGB)
        #print(result.multi_hand_landmarks)
        
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
        
        cv2.imshow('img', img)
        

    if cv2.waitKey(1) == ord('q'):
        break