import matplotlib.image as mpimg
import numpy as np
import json
import requests
from tkinter import messagebox, filedialog
import os
from matplotlib import style
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox, Style
import matplotlib
import matplotlib.pyplot as plt
import math
import weather
import geocoder
matplotlib.use("TkAgg")

#function to display figure
def showFig(event, num):

    if currentPlots[num].lower() != 'map':
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(data['time'],data[str(currentPlots[num])],'r-')
        fig.show()
    else:
        plt.imshow(
            img, extent=[pixel[0] - 640, pixel[0] + 640, pixel[1] - 400, pixel[1] + 400])
        plt.plot(data['latPixels'], data['lonPixels'], '-', color='red')
        plt.axis('off')
        plt.show()


style.use("dark_background")
#style.use("ggplot")

# set up window
root = Tk()
root.title("SOAR Ground Control")
root.iconbitmap('C:/Users/dstum/Desktop/PRT/tkinter/tutorial/rocket.ico')
root.state('zoomed')


# get width and height of maximized window
WIDTH = 1*root.winfo_screenwidth()
HEIGHT = .97*root.winfo_screenheight()
BD_THICKNESS = 0

#create base frames
top = Frame(root, width = WIDTH, height = .55*HEIGHT, bg = "white")
bottom = Frame(root, width = WIDTH, height = .45*HEIGHT, bg = "white")

top.grid(row = 0, column = 0)
bottom.grid(row = 1, column = 0)

#split top and bottom base frames
topLeft = Frame(top,width = .55*WIDTH, height = .55*HEIGHT,highlightthickness=BD_THICKNESS, bg = "white")
topRight = Frame(top,width = .45*WIDTH, height = .55*HEIGHT,highlightthickness=BD_THICKNESS, bg = "white")
bottomLeft = Frame(bottom, width = .4*WIDTH, height = .45*HEIGHT, highlightthickness=BD_THICKNESS,bg ="white")
bottomMiddle = Frame(bottom, width = .4*WIDTH, height = .45*HEIGHT, highlightthickness=BD_THICKNESS, bg = "white")
bottomRight = Frame(bottom, width = .24*WIDTH, height = .45*HEIGHT, highlightthickness=BD_THICKNESS, bg = "black")

topLeft.grid(row = 0, column = 0)
topRight.grid(row = 0, column = 1)
bottomLeft.grid(row = 0, column = 0)
bottomMiddle.grid(row = 0,column = 1)
bottomRight.grid(row = 0, column = 2)

#create final frames
mapFrame = Frame(topLeft, width=WIDTH*.55, height=.50*HEIGHT, bg="black")
mapSelectFrame = Frame(topLeft, width=.55*WIDTH, height=.05*HEIGHT,bg="black")
mapFrame.grid(row = 0, column = 0)
mapSelectFrame.grid(row = 1, column = 0)

statsSelectFrame = Frame(topRight, width = WIDTH*.27, height = .05*HEIGHT,bg = "black")
statsFrame = Frame(topRight, width = .27*WIDTH, height = .3*HEIGHT, bg = "black")
statusFrame = Frame(topRight,width = .45*WIDTH, height = .2*HEIGHT, highlightthickness=BD_THICKNESS, bg = "black")
imageFrame = Frame(topRight, width = .18*WIDTH, height = .35*HEIGHT, bg = "black")
statsSelectFrame.grid(row = 0, column = 0)
imageFrame.grid(row = 0, column = 1, rowspan = 2)
statsFrame.grid(row = 1,column = 0)
statusFrame.grid(row = 2, column = 0, columnspan = 2)

chart1Frame = Frame(bottomLeft,width = .4*WIDTH, height = .4*HEIGHT,bg="black")
chart1SelectFrame = Frame(bottomLeft,width = .4*WIDTH, height = .05*HEIGHT,bg = "black")
chart1Frame.grid(row = 0, column = 0)
chart1SelectFrame.grid(row = 1, column = 0)

chart2Frame = Frame(bottomMiddle,width = .4*WIDTH, height = .4*HEIGHT,bg="black")
chart2SelectFrame = Frame(bottomMiddle,width = .4*WIDTH, height = .05*HEIGHT,bg = "black")
chart2Frame.grid(row = 0, column = 0)
chart2SelectFrame.grid(row = 1, column = 0)

weatherFrame = Frame(bottomRight,width = .2*WIDTH, height = .35*HEIGHT,bg="black")
weatherFrame.grid(row = 0, column = 0)

alertsFrame = Frame(bottomRight, width = .2*WIDTH, height = .15*HEIGHT, bg = "black")
alertsFrame.grid(row = 1, column = 0)

#fix the size of the grids
top.grid_propagate(False)
topLeft.grid_propagate(False)
topRight.grid_propagate(False)
bottom.grid_propagate(False)
bottomLeft.grid_propagate(False)
bottomMiddle.grid_propagate(False)
bottomRight.grid_propagate(False)
statsSelectFrame.grid_propagate(False)
statsFrame.grid_propagate(False)
statusFrame.grid_propagate(False)
chart1Frame.grid_propagate(False)
chart1SelectFrame.grid_propagate(False)
chart2Frame.grid_propagate(False)
chart2SelectFrame.grid_propagate(False)
mapFrame.grid_propagate(False)
mapSelectFrame.grid_propagate(False)
weatherFrame.grid_propagate(False)
imageFrame.grid_propagate(False)
alertsFrame.grid_propagate(False)


#create figures to display graphs and map
mapFig = Figure(figsize=(.55*WIDTH/80,.5*HEIGHT/80), dpi=80)
mapAxis = mapFig.add_subplot(111)
mapLine, = mapAxis.plot([],[],'r-')

chart1Fig = Figure(figsize=(.38*WIDTH/80, .4*HEIGHT/80), dpi=80)
chart1Axis = chart1Fig.add_subplot(111)
chart1Line, = chart1Axis.plot([],[],'r-')

chart2Fig = Figure(figsize=(.38*WIDTH/80, .4*HEIGHT/80), dpi=80)
chart2Axis = chart2Fig.add_subplot(111)
chart2Line, = chart2Axis.plot([], [], 'r-')

mapAxis.set_xlabel("seconds")
chart2Axis.set_xlabel("seconds")
chart1Axis.set_xlabel("seconds")


   

#create canvases for the figures
mapCanvas = FigureCanvasTkAgg(mapFig,mapFrame)
mapCanvas._tkcanvas.grid(row=0, column=0)
mapCanvas.get_tk_widget().grid(row=0, column=0)
mapCanvas.mpl_connect('button_press_event', lambda event: showFig(event,0))

chart1Canvas = FigureCanvasTkAgg(chart1Fig,chart1Frame)
chart1Canvas._tkcanvas.grid(row = 0, column = 0)
chart1Canvas.get_tk_widget().grid(row = 0, column = 0)
chart1Canvas.mpl_connect('button_press_event', lambda event: showFig(event,1))

chart2Canvas = FigureCanvasTkAgg(chart2Fig,chart2Frame)
chart2Canvas._tkcanvas.grid(row=0, column=0)
chart2Canvas.get_tk_widget().grid(row=0, column=0)
chart2Canvas.mpl_connect('button_press_event', lambda event: showFig(event,2))

#create combobox sytle
combostyle = Style()
combostyle.theme_create('combostyle', parent='alt',
                        settings={'TCombobox':
                                  {'configure':
                                   {'selectbackground': 'red',
                                    'fieldbackground': 'red',
                                    'background': 'white'
                                    }}})
combostyle.theme_use('combostyle')

#add selection boxes
mapChoices = ['Map','Altitude','Battery Temp', 'Battery Voltages (All)',
             '3V3 Rail Voltage', '5V Rail Voltage', 'VBATT']
chartChoices = ['Altitude', 'Battery Temp',
           'Battery Voltages (All)', '3V3 Rail Voltage', '5V Rail Voltage', 'VBATT']
statsChoices = ['Pre-Flight','Flight','Post-Flight']

mapSelect = Combobox(mapSelectFrame, values=mapChoices, state='readonly')
mapSelect.place(x = 0, y = 0)
mapSelect.current(1)

chart1Select = Combobox(chart1SelectFrame, values = chartChoices, state = 'readonly')
chart1Select.place(x=0, y=0)
chart1Select.current(3)

chart2Select = Combobox(chart2SelectFrame, values=chartChoices, state='readonly')
chart2Select.place(x=0, y=0)
chart2Select.current(1)

#statsSelect = Combobox(statsSelectFrame, values = statsChoices, state = 'readonly')
#statsSelect.place(x = 0, y=0)

#upadate status lables
batt3V3 = Label(statusFrame,text="3V3 Rail Voltage:",bg = "black", foreground = "green", font=("arial",14))
batt3V3.place(x = 5, y = 5)

batt5V = Label(statusFrame, text= "5V Rail Voltage:", bg = "black", foreground = "white", font=("arial",14))
batt5V.place(x = 5, y = 45)

battV = Label(statusFrame, text="Battey Voltage:", bg="black", foreground="red", font=("arial", 14))
battV.place(x = 5, y = 85)

battTemp = Label(statusFrame, text = "Battery Temp:", bg = "black", foregroun = "yellow", font=("arial",14))
battTemp.place(x = 5, y = 125)

drougeStatus = Label(statusFrame, text = "Drouge Status:", bg = "black", foreground = "white", font=("arial",14))
drougeStatus.place(x = 350, y = 5)

mainStatus = Label(statusFrame, text = "Main Status:", bg = "black", foreground = "white", font=("arial",14))
mainStatus.place(x = 350, y = 45)

vehStatus = Label(statusFrame, text = "Vehicle Status:", bg = "black", foreground = "white", font=("arial",14))
vehStatus.place(x = 350, y = 85)


#add image and title
img = Image.open(str(os.getcwd()) + "\\assets\\logo.png")
temp = img.resize((250,250))
logoImg = ImageTk.PhotoImage(temp)
logo = Label(imageFrame, image = logoImg, bg = "black")
logo.place(x = 10, y = 0)
Label(imageFrame, text = "Ground Control", font = ("arial",20), bg = "black", foreground = "red").place(x = 35 ,y = 250)


#add labels for weather section
wImg = Image.open(str(os.getcwd())+"\\assets\\3.png")
temp = wImg.resize((150,100))
weatherImg = ImageTk.PhotoImage(temp)
img = Label(weatherFrame, image=weatherImg, bg="black", font=("arial", 12))

wthr = weather.weatherAPI()

loc = Label(weatherFrame, text = "huntsville Al", bg = "black", font=("arial", 12), foreground = "white")
curr = Label(weatherFrame, text = "Partly Cloudy", bg = "black", font=("arial", 12), foreground = "white")
temperature = Label(weatherFrame, text="Temp: 74 F", bg="black", font=("arial", 12), foreground = "white")
clouds = Label(weatherFrame, text = "ceiling: 1200  cover: 38%", bg = "black", font=("arial", 12), foreground = "white")
wind = Label(weatherFrame, text="wind: 12 mph NW", bg="black", font=("arial", 12), foreground = "white")
update = Button(weatherFrame, text = "Update", command = lambda: updateWeather(wthr))
update.config(bg="black", foreground="white", highlightthickness = 0)

img.pack(expand = True, fill = BOTH,pady = 3)
loc.pack(expand=True, fill=BOTH,pady = 3)
curr.pack(expand=True, fill=BOTH,pady = 3)
temperature.pack(expand=True, fill=BOTH,pady = 3)
clouds.pack(expand=True, fill=BOTH,pady = 3)
wind.pack(expand=True, fill=BOTH, pady=3)
update.pack(pady = 3)



#update functions
#function to update the weather pane
def updateWeather(wthr):
    
    data = wthr.getData()
    wImg = Image.open(str(os.getcwd())+"\\assets\\"+str(data['WeatherIcon'])+".png")
    temp = wImg.resize((150, 100))
    weatherImg = ImageTk.PhotoImage(temp)
    img.config(image = weatherImg)
    img.image = weatherImg

    loc.config(text = str(data['Name']))
    curr.config(text = str(data['WeatherText']))
    temperature.config(text = "Temp: " + str(data['Temperature']) + " F")
    clouds.config(text = "Ceiling: " + str(data['Ceiling']) + "  Cover: " + str(data['CloudCover']) + "%")
    wind.config(text = "Wind: " + str(data['WindSpeed']) + " mph " + str(data['WindDirection']))

def getMap(lat, lon):
    zoom = 16
    url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(lat) + "," + str(lon)+"&scale=2&zoom=" + str(
        zoom) + "&size="+str(640)+"x"+str(400)+"&maptype=satellite&key=AIzaSyAKX5P6vNDx1z29wsGwsrOzyWG842BB7DI"

    r = requests.get(url)
    f = open(str(os.getcwd())+'\\assets\\map.png', 'wb')
    f.write(r.content)
    f.close()

g = geocoder.ip('me')
print(g.latlng)
#wthr.setLocation(g.latlng[0], g.latlng[1])
#updateWeather(wthr)


log = open(str(os.getcwd()) + "\\loggylog.csv")
data = {
    'time': [],
    'battery temp': [],
    'pressure': [],
    'altitude': [],
    'eulerX': [],
    'eulerY': [],
    'eulerZ': [],
    'accelX': [],
    'accelY': [],
    'accelZ': [],
    'light': [],
    '3v3 rail voltage': [],
    '5v rail voltage': [],
    'vbatt': [],
    'lat': [],
    'lon': [],
    'latPixels': [],
    'lonPixels': []
}

currentPlots = ['altitude','altitude','3v3']

def plot0(x,y):
    mapLine.set_data(x,y)
    mapAxis.relim()
    mapAxis.autoscale_view()
    mapFig.canvas.draw()
    #mapFig.canvas.flush_events()
    
def plot1(x,y):
    chart1Line.set_data(x, y)
    chart1Axis.relim()
    chart1Axis.autoscale_view()
    chart1Fig.canvas.draw()
    #chart1Fig.canvas.flush_events()

def plot2(x,y):
    chart2Line.set_data(x, y)
    chart2Axis.relim()
    chart2Axis.autoscale_view()
    chart2Fig.canvas.draw()
    #chart2Fig.canvas.flush_events()

pixel = 0
img = None
def plotMap(lat, lon):
    global pixel, img
    mapAxis.clear()

    TILE_SIZE = 256
    zoom = 16
    scale = 1 << zoom

    worldCrd = project(lat, lon, TILE_SIZE)
    pixel = [math.floor(worldCrd[0] * scale), -math.floor(worldCrd[1] * scale)]
    
    img = mpimg.imread('assets/map.png')
    mapAxis.imshow(
        img, extent=[pixel[0] - 320, pixel[0] + 320, pixel[1] - 200, pixel[1] + 200])
    #mapAxis.plot(pixel[0], pixel[1], '-', color='red')
    mapAxis.axis('off')
    mapFig.canvas.draw()

def project(lat, lon, size):
    siny = math.sin(math.radians(lat))
    siny = min(max(siny, -.9999), .9999)

    return [size*(.5+lon/360), size*(0.5 - math.log((1 + siny) / (1 - siny)) / (4 * math.pi))]

def getPixel(lat,lon):
    TILE_SIZE = 256
    zoom = 16
    scale = 1 << zoom

    worldCrd = project(lat, lon, TILE_SIZE)
    return [math.floor(worldCrd[0] * scale), -math.floor(worldCrd[1] * scale)]

startTime = 0

def _run():
    global data, log, currentPlots, startTime, mapLine, mapAxis
    line = log.readline()

    plot0Str = mapSelect.get().lower()
    plot1Str = chart1Select.get().lower()
    plot2Str = chart2Select.get().lower()

    if plot0Str != currentPlots[0]:
        if plot0Str == 'map':
            plotMap(data['lat'][0],data['lon'][0])
            #TODO
            mapFig.suptitle('MAP')
        else:
            mapFig.clear()
            mapAxis = mapFig.add_subplot(111)
            mapLine, = mapAxis.plot([], [], 'r-')
            plot0(data['time'], data[plot0Str])
            mapFig.suptitle(plot0Str.upper())
    if plot1Str != currentPlots[1]:
        plot1(data['time'], data[plot1Str])
        chart1Fig.suptitle(plot1Str.upper())
    if plot2Str != currentPlots[2]:
        plot2(data['time'], data[plot2Str])
        chart2Fig.suptitle(plot2Str.upper())
    
    if len(line) > 1:
        t,temp,pressure,altitude,eulerX,eulerY,eulerZ,accelX,accelY,accelZ,light,_3v3,_5v,_7v4,lat,lon = line.split(',')
        if len(data['time']) < 1:
            startTime = float(t)

        data['time'].append((float(t) - startTime)/1000)
        data['battery temp'].append(float(temp))
        data['pressure'].append(float(pressure))
        data['altitude'].append(float(altitude))
        data['eulerX'].append(float(eulerX))
        data['eulerY'].append(float(eulerY))
        data['eulerZ'].append(float(eulerZ))
        data['accelX'].append(float(accelX))
        data['accelY'].append(float(accelY))
        data['accelZ'].append(float(accelZ))
        data['light'].append(float(light))
        data['3v3 rail voltage'].append(float(_3v3))
        data['5v rail voltage'].append(float(_5v))
        data['vbatt'].append(float(_7v4))
        data['lat'].append(float(lat))
        data['lon'].append(float(lon))
        data['latPixels'].append(getPixel(float(lat),float(lon))[0])
        data['lonPixels'].append(getPixel(float(lat), float(lon))[1])

        #get map image
        if len(data['lat']) == 1:
            getMap(data['lat'][0],data['lon'][0])

        #dont plot every point right away
        if len(data['time']) % 5 == 0:

            #upadate the labels with the appropriate informatin
            batt3V3.config(text="3V3 Rail Voltage: "+str(_3v3), foreground = "green" if float(_3v3) > 3.3 else ("yellow" if float(_3v3) > 3.2 else "red"))
            batt5V.config(text="5V Rail Voltage: "+str(_5v), foreground = "green" if float(_5v) > 5 else ("yellow" if float(_5v) > 4.8 else "red"))
            battV.config(text="Battery Voltage: "+str(_7v4), foreground = "green" if float(_7v4) > 7.4 else ("yellow" if float(_7v4) > 7.2 else "red"))
            battTemp.config(text = "Battery Temp: "+str(temp),foreground = "green" if float(temp) < 30 else ("yellow" if float(temp) < 40 else "red"))

            if len(data['time']) > 700:
                if len(plot0Str) > 1:
                    if plot0Str == 'map':
                        #TODO
                        #mapCanvas.draw()
                        pass
                    else:
                        plot0(data['time'][len(data['time']) - 700:],
                            data[plot0Str][len(data['time']) - 700:])
                if len(plot1Str) > 1:
                    plot1(data['time'][len(data['time']) - 700:],
                        data[plot1Str][len(data['time']) - 700:])
                if len(plot2Str) > 1:
                    plot2(data['time'][len(data['time']) - 700:],
                        data[plot2Str][len(data['time']) - 700:])
            else:
                if len(plot0Str) > 1:
                    if plot0Str == 'map':
                        #TODO
                        #mapCanvas.draw()
                        pass
                    else:
                        plot0(data['time'], data[plot0Str])
                if len(plot1Str) > 1:
                    plot1(data['time'], data[plot1Str])
                if len(plot2Str) > 1:
                    plot2(data['time'], data[plot2Str])
                    

    currentPlots[0] = plot0Str
    currentPlots[1] = plot1Str
    currentPlots[2] = plot2Str


    root.after(1,_run)


root.after(10,_run)
root.mainloop()
