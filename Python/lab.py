import cv2
import numpy as np
import os # Import the os module
model_proto=r"C:\Users\Admin\Desktop\New folder (2)\images.jpg"
model_weights = r"C:\Users\Admin\Desktop\New folder (2)\images.jpg"

# Check if the prototxt file exists
if not os.path.exists(model_proto):
    print(f"Error: prototxt file not found at {model_proto}")
    exit() # Exit if the file doesn't exist

# Load the model
try:
    net = cv2.dnn.readNetFromCaffe(model_proto, model_weights)
except cv2.error as e:
    print(f"Error loading the model: {e}")
    exit()


# Class labels for the model
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Load the image
image_path = r"C:\Users\Admin\Desktop\New folder (2)\images.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the image. Please check the file path.")
else:
    (h, w) = image.shape[:2]

    # Convert image to blob format
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    confidence_threshold = 0.5
    boxes = []
    confidences = []
    class_ids = []

    # Loop through detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            boxes.append([startX, startY, endX - startX, endY - startY])
            confidences.append(float(confidence))
            class_ids.append(idx)

    # Apply Non-Maximum Suppression (NMS)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.4)

    if len(indices) > 0:
        for i in indices.flatten():
            (startX, startY, width, height) = boxes[i]
            endX = startX + width
            endY = startY + height
            label = f"{CLASSES[class_ids[i]]}: {confidences[i] * 100:.2f}%"

            # Draw bounding box and label
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(image, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Show the image with detections
    cv2.imshow("Object Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the output image
    output_path = r"/content/images.jpg"
    cv2.imwrite(output_path, image)
    print(f"Output saved at: {output_path}")
