
import cv2
import mediapipe as mp
import math
import numpy as np

class HandGestureRecognizer:
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5)
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.gestures = {
            0: "Fist",
            1: "Open Hand",
            2: "Pointing",
            3: "Victory",
            4: "Rock",
            5: "Thumbs Up",
            6: "Thumbs Down",
            7: "OK"
        }
    
    def calculate_distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
    def recognize_gesture(self, landmarks):
        # Thumb checks
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        thumb_mcp = landmarks[2]
        
        # Index finger
        index_tip = landmarks[8]
        index_dip = landmarks[7]
        index_pip = landmarks[6]
        index_mcp = landmarks[5]
        
        # Middle finger
        middle_tip = landmarks[12]
        middle_dip = landmarks[11]
        middle_pip = landmarks[10]
        middle_mcp = landmarks[9]
        
        # Ring finger
        ring_tip = landmarks[16]
        ring_dip = landmarks[15]
        ring_pip = landmarks[14]
        ring_mcp = landmarks[13]
        
        # Pinky finger
        pinky_tip = landmarks[20]
        pinky_dip = landmarks[19]
        pinky_pip = landmarks[18]
        pinky_mcp = landmarks[17]
        
        # Wrist
        wrist = landmarks[0]
        
        # Calculate finger states
        thumb_extended = thumb_tip.y < thumb_ip.y
        index_extended = index_tip.y < index_pip.y
        middle_extended = middle_tip.y < middle_pip.y
        ring_extended = ring_tip.y < ring_pip.y
        pinky_extended = pinky_tip.y < pinky_pip.y
        
        # Gesture recognition logic
        if not thumb_extended and not index_extended and not middle_extended and not ring_extended and not pinky_extended:
            return 0  # Fist
        
        if thumb_extended and index_extended and middle_extended and ring_extended and pinky_extended:
            return 1  # Open Hand
        
        if index_extended and not middle_extended and not ring_extended and not pinky_extended:
            if thumb_extended:
                return 2  # Pointing
            else:
                return 2  # Pointing (thumb not extended)
        
        if not index_extended and middle_extended and not ring_extended and not pinky_extended:
            return 3  # Victory
        
        if index_extended and pinky_extended and not middle_extended and not ring_extended:
            return 4  # Rock
        
        if thumb_extended and not index_extended and not middle_extended and not ring_extended and not pinky_extended:
            # Check thumb direction (up or down)
            thumb_vector = np.array([thumb_tip.x - wrist.x, thumb_tip.y - wrist.y])
            reference_vector = np.array([1, 0])  # Horizontal right
            
            angle = math.degrees(math.atan2(thumb_vector[1], thumb_vector[0]))
            if angle < -45:
                return 5  # Thumbs Up
            else:
                return 6  # Thumbs Down
        
        if thumb_extended and index_extended and not middle_extended and not ring_extended and not pinky_extended:
            # Check if thumb and index form a circle (OK sign)
            distance = self.calculate_distance(thumb_tip, index_tip)
            thumb_index_base_dist = self.calculate_distance(thumb_mcp, index_mcp)
            if distance < thumb_index_base_dist * 0.5:
                return 7  # OK
        
        return -1  # Unknown gesture
    
    def process_frame(self, frame):
        # Convert the BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the image and find hands
        results = self.hands.process(image)
        
        # Draw hand landmarks
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                self.mp_drawing.draw_landmarks(
                    image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Recognize gesture
                gesture_id = self.recognize_gesture(hand_landmarks.landmark)
                if gesture_id != -1:
                    # Get hand bounding box
                    h, w, _ = image.shape
                    landmarks = hand_landmarks.landmark
                    x_coords = [lm.x * w for lm in landmarks]
                    y_coords = [lm.y * h for lm in landmarks]
                    min_x, max_x = int(min(x_coords)), int(max(x_coords))
                    min_y, max_y = int(min(y_coords)), int(max(y_coords))
                    
                    # Display gesture text
                    cv2.putText(image, self.gestures[gesture_id], 
                               (min_x, min_y - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        return image
    
    def run(self):
        cap = cv2.VideoCapture(0)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # Flip the frame horizontally for a mirror effect
            frame = cv2.flip(frame, 1)
            
            # Process the frame
            processed_frame = self.process_frame(frame)
            
            # Display the processed frame
            cv2.imshow('Hand Gesture Recognition', processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recognizer = HandGestureRecognizer()
    recognizer.run()
