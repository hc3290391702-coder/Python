from abc import ABC, abstractmethod



'''
facede
class CPU:
    def start(self):
        print("CPU start")

class Memory:
    def load(self):
        print("Memory load")

class HardDrive:
    def read(self):
        print("HardDrive read")



class Computer_Start:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._harddrive = HardDrive()


    def computer_start(self):
        self._cpu.start()
        self._memory.load()
        self._harddrive.read()

    def CPU_start(self):
        self._cpu.start()


computer = Computer_Start()
computer.computer_start()
computer.CPU_start()


'''
#通过Computer_Start将三个类CPU，Memory，HardDrive进行封装，只有一个computer_start作为对外接口。
#用户不需要分别调用各个组件的方法，也不需要了解它们之间的调用顺序，
#只需调用一个方法即可完成整个启动流程。这样可以有效降低系统复杂性，提高代码的可读性和易用性，同时减少客户端与子系统之间的耦合

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#strategy

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Credit Card Pay: {amount}")


class PaypalPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paypal Pay: {amount}")

class CryptoPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Crypto Pay: {amount}")



#负责使用策略（strategy），但不关心具体策略的实现。
#需要完成的事情是实现checkout()

class ShoppingCart:
#初始化__init__
    def __init__(self,strategy: PaymentStrategy):
        self.strategy = strategy

#更换策略set_strategy()
    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

#checkout()
    def checkout(self, amount):
        print("check out")
        self.strategy.pay(amount)

def main():
    # create context with initial strategy
    cart = ShoppingCart(PaypalPayment())
    cart.checkout(150)

    # change strategy
    cart.set_strategy(CreditCardPayment())
    cart.checkout(250)

    # change strategy again
    cart.set_strategy(CryptoPayment())
    cart.checkout(350)

if __name__ == "__main__":
    main()

'''这段代码展示了策略模式。
PaymentStrategy 定义了所有支付方法共同的接口。
CreditCardPayment、PayPalPayment 和 CryptoPayment 是具体策略类，分别实现不同的支付方式。
ShoppingCart 是上下文类，它通过组合一个策略对象来完成支付。
在运行过程中可以灵活替换策略，而不需要修改上下文类。'''

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#command

#定义light类，有开关两个功能
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

'''RemoteControl 是 Command Pattern 中的 Invoker（调用者）。
它保存一个命令对象，并在按钮被按下时触发该命令。
set_command() 方法用于给遥控器设置命令，而 press_button() 通过调用 command.execute() 来执行该命令。
遥控器不需要知道具体的操作逻辑，从而降低了调用者和接收者之间的耦合。'''


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#Template


#定义饮料类，Beverage, 其中有准备prepare(),是所有饮料有的步骤
class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("water boiling")
    @abstractmethod
    def brew(self):
        pass
    @abstractmethod
    def add_condiments(self):
        pass
    def pour_in_cup(self):
        print("pouring cup")

#coffee类，重写brew和add_condiments

class Coffee(Beverage):
    def brew(self):
        print("coffee brewing")
    def add_condiments(self):
        print("add milk and suger")

#Tea类，重写brew和add_condiments

class Tea(Beverage):
    def brew(self):
        print("tea brewing")
    def add_condiments(self):
        print("add lemon")

#
coffee = Coffee()
tea = Tea()

coffee.prepare()
tea.prepare()

#模版中父类定义了算法结构，允许子类继承并改写
#Template核心思想：在父类中定义算法的整体流程（template），把具体步骤的实现留给子类完成

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————

