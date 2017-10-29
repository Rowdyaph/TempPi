from gpiozero import CPUTemperature 
from time import sleep, strftime, time
import matplotlib.pyplot as plt

temp = CPUTemperature()

plt.ion()
x=[]
y=[]

def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        
def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(X,Y)
    plt.draw()
            
            
while true:
    temp = cpu.temperature()      
              
        sleep(1)
        
#automating the script
        
        