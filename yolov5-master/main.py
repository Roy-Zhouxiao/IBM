import cv2
import detect

# m_detect = detect.detectapi(weights='D:/yolo data/best.pt')

# video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# while True:
#     rec, image = video_capture.read()
#     result, names = m_detect.detect([image])
#     image = result[0][0]  # 第一张图片的处理结果图片
#     for cls, (x1, y1, x2, y2), conf in result[0][1]:  # 第一张图片的处理结果标签。
#         print(cls, x1, y1, x2, y2, conf)
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0))
#         cv2.putText(image, names[cls], (x1, y1 - 20), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0))
#     cv2.imshow("video", image)
#     if cv2.waitKey(1) == ord('q'):
#         break

# video_capture = cv2.VideoCapture('D:/data/videos/plane (1).mp4')
# while (video_capture.isOpened()):
#     ret, image = video_capture.read()
#     if not ret:
#         print('获取视频流失败')
#         break
#     result, names = m_detect.detect([image])
#     image = result[0][0]  # 第一张图片的处理结果图片
#     for cls, (x1, y1, x2, y2), conf in result[0][1]:  # 第一张图片的处理结果标签。
#         print(cls, x1, y1, x2, y2, conf)
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0))
#         cv2.putText(image, names[cls], (x1, y1 - 20), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0))
#     cv2.imshow("video", image)
#     if cv2.waitKey(1) == ord('q'):
#         break
#     video_capture.release()
#     cv2.destroyAllWindows()

# image=cv2.imread('D:/data/pictures/plane (1).jpg')
# result, names = m_detect.detect([image])
# image = result[0][0]  # 第一张图片的处理结果图片
# for cls, (x1, y1, x2, y2), conf in result[0][1]:  # 第一张图片的处理结果标签。
#     print(cls, x1, y1, x2, y2, conf)
#     cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0))
# cv2.putText(image, names[cls], (x1, y1 - 20), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0))
# cv2.imshow("video", image)


# cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap = cv2.VideoCapture('D:/data/videos/plane (2).mp4')
a = detect.detectapi(weights='D:/yolo data/best.pt')
while True:
    rec, img = cap.read()
    result, names = a.detect([img])
    img = result[0][0]  # 第一张图片的处理结果图片
    for cls,(x1,y1,x2,y2),conf in result[0][1]: #第一张图片的处理结果标签。
        print(cls,x1,y1,x2,y2,conf)
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0))
        # cv2.putText(img,names[cls],(x1,y1-20),cv2.FONT_HERSHEY_DUPLEX,1.5,(255,0,0))
    cv2.imshow("video", img)
    if cv2.waitKey(1) == ord('q'):
        break
