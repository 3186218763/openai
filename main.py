<<<<<<< HEAD
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

#调用要使用的模型
mpHands = mp.solutions.hands #处理手部的模型
mpDraw = mp.solutions.drawing_utils #绘制模型

#设置使用模型的具体的参数
hands = mpHands.Hands(min_detection_confidence=0.8) #设置处理手部模型参数
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=5)  #设置绘制点模型的参数
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=3)  #设置绘制线模型的参数

pTime = 0
cTime = 0


while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #把RGB图片交给设置好的模型处理
        result = hands.process(imgRGB)
        #print(result.multi_hand_landmarks)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                #怎么获取每个点的坐标
                for i, lm in enumerate(handLms.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    #在图片上标注每个点的位置
                    cv2.putText(img, str(i), (xPos - 25, yPos + 5), cv2.FONT_HERSHEY_PLAIN, 0.6, (255, 0, 0), 1)
                    print(i, xPos, yPos)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, "FPS: " + str(int(fps)), (30, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 3)
        cv2.imshow('img', img)
        

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
=======
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

#调用要使用的模型
mpHands = mp.solutions.hands #处理手部的模型
mpDraw = mp.solutions.drawing_utils #绘制模型

#设置使用模型的具体的参数
hands = mpHands.Hands(min_detection_confidence=0.8) #设置处理手部模型参数
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=5)  #设置绘制点模型的参数
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=3)  #设置绘制线模型的参数

pTime = 0
cTime = 0


while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #把RGB图片交给设置好的模型处理
        result = hands.process(imgRGB)
        #print(result.multi_hand_landmarks)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                #怎么获取每个点的坐标
                for i, lm in enumerate(handLms.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    #在图片上标注每个点的位置
                    cv2.putText(img, str(i), (xPos - 25, yPos + 5), cv2.FONT_HERSHEY_PLAIN, 0.6, (255, 0, 0), 1)
                    print(i, xPos, yPos)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, "FPS: " + str(int(fps)), (30, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 3)
        cv2.imshow('img', img)
        

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
>>>>>>> b27a7cec4ec6eac550b6373d8673bc5879668481
cv2.destroyAllWindows()