# What is this??
- I had a rc car lying around my house and my keyboard, so i thought why not use the keyboard to control it.
- so i modified the orignal rc car so that it can be controlled with my pc.


# How does it works?
- In my case the original Rc car had only 4 types of directional input i.e. left,right, up, down
- so i used ESP8266 with micropython and used each digital pin to control the directional inputs
- since in my case there was no speed contorl  in orignnal hardware things were easier. 
- You can see the image to get better idea.
![alt text](<image/circuit.png>)


# What next ?
- i would like to use sensors to control the car but currently the control and their output are not stardized , as i said there is no speed control in this car.
- Modifying the hardware to get speed control will be a hastle so i will try to create a script which can contorl the speed.
## Speed control
- Currently i can use timing to achieve something simiar to speed contorl, what is mean in that the switch will be on for a certain time  and then turn off and this repeated behaviour can be used to control speed. 
- or if anyone want to  modify hardware they can use something similar to dual mosfet configuration to control the speed(motor) but as i said i don't want to modify the original car's hardware.


# Notations
- The board.py file will be flashed to micrpython device(esp8266 in our case) 
and the server.py file can be used to connect to the board.
- Please edit the ip address according to your network

# Tasks
- [ ] create a speed contorl script
- [ ] control the car using a sensor like HCSR04, 
- [ ] create neural network to control the car,, (yeah i guess i will do it but cheap camera like esp32 cam are not good and unreliable, lets see what can we use.)