import time


class TrafficLight:

    def __init__(self):
        self.__light_color = ['red', 'yellow', 'green']
        self.a = 0

    def running(self):
        print(f'Now color {self.__light_color[0]}')

    def switch_color(self):
        while True:
            if self.a == 0:
                self.a += 1
                time.sleep(7)
            elif self.a == 1:
                self.a += 1
                time.sleep(2)
            elif self.a == 2:
                self.a = 0
                time.sleep(5)


if __name__ == '__main__':
    new_trafficlight = TrafficLight()
    new_trafficlight.running()
    new_trafficlight.switch_color()
