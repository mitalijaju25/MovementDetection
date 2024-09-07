# MovementDetection

# Project Overview
This project integrates two MPU9250 motion sensors with an Arduino UNO board to collect real-time motion data. The data is then transmitted to an application layer built using the Django framework, where it is efficiently processed and visualized. This system demonstrates how hardware and web technologies can be combined for real-time data analysis and monitoring.

# Features
- Real-Time Motion Data Collection: Two MPU9250 sensors collect motion data such as acceleration and angular velocity.
- Arduino Control: The sensors are interfaced with the Arduino UNO, which reads the data and transfers it to the Django framework.
- Django Integration: The data collected by the Arduino is transferred to Django for processing, visualization, and rendering on a web interface
- Data Visualization: The Django web application presents real-time data in a user-friendly interface, offering insights into the motion detected by the sensors.

# Project Components
Hardware: Arduino UNO board, 2 MPU9250 motion sensors, Jumper wires and breadboard
Software: Arduino IDE (for sensor control), VisualStudio2022 (for data handling, processing, and visualization)

# Django Files Breakdown
Here’s an overview of the important files used in the Django application layer:

- manage.py:
This file is responsible for the management of the Django project. It provides the command-line utility to execute various administrative tasks, such as running the server, migrating the database, and more.

- views.py:
Contains the logic of the application. It processes the data transferred from the Arduino, structures it, and passes it to the appropriate templates for rendering. This file is responsible for taking motion sensor data and preparing it for display or further processing.

- urls.py:
Defines the URL routes of the Django application. It maps specific URLs to corresponding view functions in views.py, making sure that requests are routed to the correct part of the application.
  
- index.html:
This is the front-end template where the processed data is visualized. It contains HTML and Django template language to render dynamic content like motion graphs or sensor readings based on the data passed from the backend.

- settings.py:
Manages the configuration settings of the Django project. This includes database connections, static files, installed apps, middleware, and other important parameters required for the application to run smoothly.

# How it Works
- Motion Data Collection: The two MPU9250 sensors are connected to the Arduino UNO board, which reads the motion data (e.g., acceleration, gyroscope data).
- Data Transmission: The data collected is then transferred to the Django framework through serial communication.
- Data Processing in Django: Django processes the incoming data, stores it, and visualizes it on the front-end using index.html.
- Visualization: The motion sensor data is displayed on a web interface, providing real-time feedback to the user.
