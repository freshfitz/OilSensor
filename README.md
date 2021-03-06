# OilSensor
Python pi ultrasonic distance sensor used as tank sensor to output levels to a json feed

{"percentage": 76.3988548810431, "gals": 190.99713720260775, "name": "OilSensor", "cm": 37.83, "in": 14.893700787401574}

<img src="https://github.com/freshfitz/OilSensor/blob/main/Capture.JPG">
<img src="https://github.com/freshfitz/OilSensor/blob/main/Capture1.JPG">

This is a python script to output the distance of a tank sensor to tank gallons left and percentage of tank full. I am using the script to display the results on my magic mirror.

Connect sensor to your pi
<img src="https://pi.lbbcdn.com/wp-content/uploads/2018/03/Distance-sensor-GPIO-pins-768x147.png">


To install you must install apache and php on your pi
from your home directory ~/pi run


git clone https://github.com/freshfitz/OilSensor 

To install apache and php run

sudo apt install apache2 -y

sudo apt install php libapache2-mod-php -y

this script will use index.php to display the json so first lets remove the default index.html

rm -rf /var/www/html/index.html

#Create index.php

touch /var/www/html/index.php

#allow index.php writeable from the python script

chown -R pi:pi /var/www/html/index.php

chmod 777 /var/www/html/index.php

#If you have your sensor connected to your pi run 

python ~/OilSensor/sensor.py

You should get an output of

pi@oilsensor:~ $ python ~/oilsensor/sensor.py

Waiting for sensor to settle

Calculating distance

Distance: 37.46 cm

Distance: 14.7480314961 in

Gallons: 192.220837567 US

Percentage: 76.8883350267 %


if you browse to your pi's ip address you should get http://ip-of-pi

{"percentage": 76.3988548810431, "gals": 190.99713720260775, "name": "OilSensor", "cm": 37.83, "in": 14.893700787401574}

Look at the top lines of sensor.py you will have to adjust the distances for your setup and the tank size for your setup

You can now use anything you want to read this json format, for example I have it displaying on my magicmirror using MMM-Json-feed
https://github.com/amcolash/MMM-json-feed

To update the data I have a cron job running, simply use

crontab -e

*/5 * * * * python ~/oilsensor/sensor.py

this will run the script every 5 min and update the index.php file


