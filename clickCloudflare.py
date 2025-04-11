import pyautogui
import time
import random

def get_bezier_points(start, control1, control2, end, steps=30):
    """
    Calculate a list of points along a cubic Bézier curve.
    
    :param start: Tuple (x, y) for the starting point.
    :param control1: Tuple (x, y) for the first control point.
    :param control2: Tuple (x, y) for the second control point.
    :param end: Tuple (x, y) for the end point.
    :param steps: Number of points to generate.
    :return: List of tuples (x, y) representing points along the curve.
    """
    points = []
    for i in range(steps + 1):
        t = i / steps
        # Cubic Bézier formula:
        x = (1 - t)**3 * start[0] + 3 * (1 - t)**2 * t * control1[0] + 3 * (1 - t) * t**2 * control2[0] + t**3 * end[0]
        y = (1 - t)**3 * start[1] + 3 * (1 - t)**2 * t * control1[1] + 3 * (1 - t) * t**2 * control2[1] + t**3 * end[1]
        points.append((x, y))
    return points

# Introduce a random delay before starting.
time.sleep(random.uniform(1, 3))

# Locate the target image on the screen.
location = pyautogui.locateOnScreen('cloudflareImage.png', confidence=0.9)

if location:
    # Get the center of the located image.
    center = pyautogui.center(location)
    
    # Randomize the final target within a ±5 pixel radius.
    target = (center.x + random.randint(-5, 5), center.y + random.randint(-5, 5))
    
    # Get the current mouse position as the starting position.
    start_position = pyautogui.position()
    
    # Random control points determine the curvature of the path.
    # The control points are chosen with an offset range to create a nice curve.
    control1 = (start_position[0] + random.randint(-100, 100), start_position[1] + random.randint(-100, 100))
    control2 = (target[0] + random.randint(-100, 100), target[1] + random.randint(-100, 100))
    
    # Generate the Bézier curve points.
    bezier_points = get_bezier_points(start_position, control1, control2, target, steps=30)
    
    # Move the mouse along the computed curve.
    # Adjust the duration per move as desired to control overall speed.
    for point in bezier_points:
        pyautogui.moveTo(point[0], point[1], duration=0.01)
    
    # Click at the final target position.
    pyautogui.click()
else:
    print("Image not found.")
