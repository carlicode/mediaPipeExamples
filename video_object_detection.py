import cv2
import time

def draw_colored_rectangle(frame, color):
    height, width, _ = frame.shape
    top_left = (width // 4, height // 4)
    bottom_right = (3 * width // 4, 3 * height // 4)

    if color == 'red':
        rectangle_color = (0, 0, 255)  # Red color in BGR
    elif color == 'blue':
        rectangle_color = (255, 0, 0)  # Blue color in BGR

    cv2.rectangle(frame, top_left, bottom_right, rectangle_color, thickness=2)

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)

    color_sequence = ['red', 'blue']  # Red, blue, red, blue, ...

    interval = 0.025  # Interval of 0.025 seconds

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        color = color_sequence[int(time.time() / interval) % 2]  # Alternating between red and blue
        
        draw_colored_rectangle(frame, color)
        
        cv2.imshow('Video with Rectangles', frame)
        
        if cv2.waitKey(int(1000 * interval)) & 0xFF == ord('q'):  # Display frame for interval, exit on 'q' key
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    video_path = 'cats_dogs.mp4'  # Reemplaza con la ruta de tu video
    main(video_path)
