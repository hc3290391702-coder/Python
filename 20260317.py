from abc import ABC, abstractmethod

class Light:
    def turn_on(self):
        print("light turn on")
    def turn_off(self):
        print("light turn off")

#Command Interface
class Command(ABC):
    @abstractmethod
    def excuate(self):
        pass

#LightOnCommand
class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light
    def excuate(self):
        self.light.turn_on()

#lightOffCommand
class LightOffCommand(Command):
    def __init__(self,light):
        self.light = light
    def excuate(self):
        self.light.turn_off()

#遥控器类，发出命令，但不执行具体操作
class RemoteControl:
    def set_command(self,command):
        self.command = command
    def press_button(self):
        self.command.excuate()


if __name__ == '__main__':
    light = Light()  #灯类
    light_on = LightOnCommand(light)  #开灯类
    light_off = LightOffCommand(light)   #关灯类

    remote = RemoteControl()    #遥控器类

    remote.set_command(light_on)   #遥控器开灯，执行按钮方法
    remote.press_button()
    remote.set_command(light_off)  #遥控器关灯，执行按钮方法
    remote.press_button()