from ultralytics import YOLO
import cv2

# 모델 로드
model1 = YOLO("./best.pt")
model2 = YOLO('./train4/weights/best.pt')

# Haar Cascade 로드
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 비디오 캡처 객체 생성 (0번 카메라 사용)
cap = cv2.VideoCapture(0)

# 비디오 캡처가 열려 있는 동안 루프 실행
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 얼굴 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # 얼굴 영역 추출
        face_roi = frame[y:y+h, x:x+w]

        # 첫 번째 모델 예측
        results1 = model1.predict(
            source=face_roi, save=False, imgsz=640, conf=0.6)

        detection_found = False

        # 모델 1 결과 처리
        for r in results1:
            if len(r.boxes) > 0:
                detection_found = True
                boxes = r.boxes.xyxy
                cls = r.boxes.cls
                conf = r.boxes.conf
                cls_dict = r.names

                for box, cls_number, conf in zip(boxes, cls, conf):
                    cls_name = cls_dict[int(cls_number.item())]
                    x1, y1, x2, y2 = box
                    x1_int, y1_int, x2_int, y2_int = map(int, box)
                    print(x1_int, y1_int, x2_int, y2_int, cls_name)

                    # 원본 이미지에 좌표값 조정
                    x1_scale = x + int(x1_int * (w / 640))
                    y1_scale = y + int(y1_int * (h / 640))
                    x2_scale = x + int(x2_int * (w / 640))
                    y2_scale = y + int(y2_int * (h / 640))

                    frame = cv2.rectangle(
                        frame, (x1_scale, y1_scale), (x2_scale, y2_scale), (0, 225, 0), 2)
                    frame = cv2.putText(frame, f"{cls_name} (Model 1)", (x1_scale, y1_scale - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # 첫 번째 모델에서 감지되지 않은 경우 두 번째 모델 사용
        if not detection_found:
            results2 = model2.predict(
                source=face_roi, save=False, imgsz=640, conf=0.6)
            for r in results2:
                if len(r.boxes) > 0:
                    detection_found = True
                    boxes = r.boxes.xyxy
                    cls = r.boxes.cls
                    conf = r.boxes.conf
                    cls_dict = r.names

                    for box, cls_number, conf in zip(boxes, cls, conf):
                        cls_name = cls_dict[int(cls_number.item())]
                        x1, y1, x2, y2 = box
                        x1_int, y1_int, x2_int, y2_int = map(int, box)
                        print(x1_int, y1_int, x2_int, y2_int, cls_name)

                        # 원본 이미지에 좌표값 조정
                        x1_scale = x + int(x1_int * (w / 640))
                        y1_scale = y + int(y1_int * (h / 640))
                        x2_scale = x + int(x2_int * (w / 640))
                        y2_scale = y + int(y2_int * (h / 640))

                        frame = cv2.rectangle(
                            frame, (x1_scale, y1_scale), (x2_scale, y2_scale), (0, 225, 0), 2)
                        frame = cv2.putText(frame, f"{cls_name} (Model 2)", (x1_scale, y1_scale - 10),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # 두 모델에서 모두 감지되지 않은 경우
        if not detection_found:
            cv2.putText(frame, "NOT OUR CLASS", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # 결과 프레임 출력
    cv2.imshow("Live Detection", frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 객체 및 모든 윈도우 종료
cap.release()
cv2.destroyAllWindows()
