import cv2
import numpy as np

# Read the image
img1 = cv2.imread('shapes.jpg')
img2 = cv2.imread('shapes.jpg')

# Convert to grayscale
img1Grey = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thrash = cv2.threshold(img1Grey, 240, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Save the original labeled image
cv2.imwrite("OriginalOne.jpg", img1)

# Create a mask to remove all non-star shapes
mask = np.zeros(img1.shape[:2], dtype=np.uint8)  # Black mask (0 means remove, 255 means keep)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img1, [approx], 0, (0, 0, 0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv2.putText(img1, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.drawContours(mask, [contour], 0, 0, -1)  # Remove triangle (set mask to 0)

    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h

        if 0.95 <= aspectRatio <= 1.05:
            cv2.putText(img1, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img1, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        cv2.drawContours(mask, [contour], 0, 0, -1)  # Remove square/rectangle

    elif len(approx) == 5:
        cv2.putText(img1, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.drawContours(mask, [contour], 0, 0, -1)  # Remove pentagon

    elif len(approx) == 10:
        cv2.putText(img1, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.drawContours(mask, [contour], 0, 255, -1)  # Keep the star (set mask to 255)

    else:
        cv2.putText(img1, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.drawContours(mask, [contour], 0, 0, -1)  # Remove circle

# Save the labeled image
cv2.imwrite("NamesShapes.jpg", img1)

# Convert mask to 3 channels
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

# Apply the mask to remove all shapes except the star
result = cv2.bitwise_and(img2, mask)  # Keeps only the star

# Save the final image with only the star remaining
cv2.imwrite("OnlyStar.jpg", result)
