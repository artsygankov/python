# Program to create class trafficlight
from time import sleep


class Trafficlight:
    __color = 'Белый'

    def running(self):
        in_color = in_seconds = ''
        trafficlight_settings_list = ['Красный-7', 'Желтый-2', 'Зеленый-5', 'Желтый-2']
        while True:
            for element in trafficlight_settings_list:
                in_color, in_seconds = element.split('-')
                print(f'\r{in_color}', end='')
                sleep(int(in_seconds))


TrafficLight = Trafficlight()
TrafficLight.running()
