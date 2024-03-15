import cv2 as cv
from deepface import DeepFace
import os 

def extraction(i):
    capture = cv.VideoCapture(0)
    while True:
        success, frame = capture.read()

        if not success:
            print("Erro ao ler o frame")
            print("Tente novamente")
            break
        
        cv.imshow("Photo", frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            print("Camera fechada")
            break

    cv.destroyAllWindows()
    capture.release()
    for i in range(1,5):
        cv.waitKey(1)
        
    
    i = i + 1
    return frame



def data_base_analyze(data):
    directory = "img"
    lista2 = []
    for i, file in enumerate(os.listdir(directory)):
        results = DeepFace.analyze(f"img/img{i+1}.jpg")
        if results:
            print("Age: ", results[0]["age"])
            print("Gender: ", results[0]["gender"])
            print("Emotion: ", results[0]["dominant_emotion"])
            print("Race: ", results[0]["dominant_race"])
            points = 0
            if results[0]["dominant_emotion"] == data[0]:
                points += 1
            elif results[0]["age"] == data[1]:
                points += 1
            elif results[0]["gender"] == data[2]:
                points += 1
            elif results[0]["dominant_race"] == data[3]:
                points += 1
            
            lista2.append(points)
            print(lista2)
    big_matching = max(lista2)
    index = lista2.index(big_matching)
    return index


def verify():
    frame_CF = extraction()
    cv.imwrite("img_find/img.jpg", frame_CF)
    for i in enumerate(os.listdir("img")):
        i += 1
        results = DeepFace.verify("img_find/img.jpg", f"img/img{i}.jpg")
        print(results["verify"])
        if results["verify"] == True:
            os.remove("img_find/img.jpg")
            return i
