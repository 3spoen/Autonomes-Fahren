# Lane Detection System

## Overview
This project implements a lane detection system using Python, OpenCV, and NumPy. It processes video input to identify and highlight lane lines on the road in real time. The system uses Canny edge detection, region of interest selection, and Hough transform line detection to analyze the frames of the video and output a visualization of the detected lane lines.

## Features
- **Canny Edge Detection**: Converts frames to grayscale and identifies edges in the image.
- **Region of Interest Masking**: Isolates the area of the frame where lane lines are expected, reducing noise from other objects.
- **Line Detection with Hough Transform**: Finds line segments in the masked edge-detected image.
- **Averaging and Extrapolation**: Processes detected lines to create a single average line for each lane boundary.
- **Real-Time Lane Overlay**: Overlays detected lane lines onto the original video frames in real time.

## Dependencies
- Python 3.x
- OpenCV (cv2)
- NumPy
- Matplotlib (optional, for debugging or visualization)

## Setup
Ensure you have Python 3.x installed on your system. Install the required Python packages using pip:

```sh
pip install numpy opencv-python matplotlib
```

## Usage
To run the lane detection system, ensure you have a video file (e.g., `test_video.mp4`) in the project directory. Modify the `cap = cv2.VideoCapture("test_video.mp4")` line in the script to point to your video file.

Run the script with Python:

```sh
python lane_detection.py
```

Press `q` to quit the video playback window.

## How It Works
1. **Frame Processing**: Each frame of the video is converted to grayscale, blurred using a Gaussian filter, and edges are detected using the Canny edge detector.
2. **Masking**: A region of interest is defined to focus on the part of the image where lanes are expected, reducing distractions from other parts of the image.
3. **Line Detection**: The Hough Transform is applied to detect lines within the defined region of interest.
4. **Line Averaging and Extrapolation**: Detected lines are separated into left and right lanes based on their slope. Lines are then averaged and extrapolated to cover the full lane marking.
5. **Overlay**: The averaged lines are drawn onto the original frame, visually indicating the position of lane lines.

## Contributing
Contributions to improve the lane detection system are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE.md).

---

Remember to include any additional instructions or information specific to your project that users might need to know.
