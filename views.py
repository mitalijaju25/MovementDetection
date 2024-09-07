# # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import View
import serial
import json
from django.http import JsonResponse





import serial
import json
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def getind(request):
    return render(request, 'imu/index.html')

class IMUView(View):
    def get(self, request):
        try:
                   # Open the serial connection
            ser = serial.Serial('COM4', 9600)  # Adjust the port accordingly

            # Read data from the serial port
            data = ser.readline().decode().strip()

            # Close the serial connection
            ser.close()

            # Parse the received data
            values = data.split('/')

            # Extract the accelerometer and gyro values
            roll1 = float(values[0])
            pitch1 = float(values[1])
            yaw1 = float(values[2])
            roll2 = float(values[3])
            pitch2 = float(values[4])
            yaw2 = float(values[5])


            # Process the data as needed
            # ...

            # Render the template with the received data
            context = {
                'roll1': roll1,
                'pitch1': pitch1,
                'yaw1': yaw1,
                'roll2': roll2,
                'pitch2': pitch2,
                'yaw2': yaw2,
            }

            json_data = json.dumps(context)
            return JsonResponse(context, safe=False)
        except Exception as e:
            logger.error("An error occurred while reading from the serial port: %s", str(e))
            return JsonResponse({'error': 'Failed to read data from the serial port'}, status=500)
