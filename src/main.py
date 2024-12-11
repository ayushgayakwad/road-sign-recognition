import cv2
from yolov5 import YOLOv5

weights_path = r"model\weights\best.pt"
yolo = YOLOv5(weights_path, device="cpu") 

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = yolo.predict(frame) 

    confidence_threshold = 0.54

    if results.xyxy is not None and len(results.xyxy):
        detections = results.xyxy[0] 
        for box in detections:  
            if len(box) >= 6:
                x1, y1, x2, y2, conf, cls = box.tolist()
                
                if conf >= confidence_threshold:  
                    label = f"{results.names[int(cls)]} {conf:.2f}"
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Road Sign Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
