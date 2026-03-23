from abc import ABC, abstractmethod
from os import statvfs_result
from urllib.request import ProxyHandler


#Composite
#文件系统类（FileSystemComponent）
class FileSystemComponent(ABC):
    def show(self,indent = 0):
        pass

#文件类File（继承文件系统类）
#__Init__, show(根据缩进层级打印文件名)
class File(FileSystemComponent):
    def __init__(self,name):
        self.name = name
    def show(self,indent = 0):
        print(" " * indent + f"File: {self.name}")

#文件夹类Folder（继承文件系统类）
#__init__(name,stream),
#add 方法，remove方法，show方法
class Folder(FileSystemComponent):
    def __init__(self,name):
        self.name = name
        self.stream = []
    def add(self,component):
        self.stream.append(component)
    def remove(self,component):
        self.stream.remove(component)
    def show(self,indent = 0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.stream:
            child.show(indent + 4)


file1 = File("file1")
file2 = File("file2")
file3 = File("file3")

folder1 = Folder("folder")
folder2 = Folder("folder2")

folder1.add(file1)  #folder1----file1
folder2.add(file2)  #folder2----file2
folder1.add(file3)  #folder1----file2--file3
root = Folder("root")

root.add(folder1)
root.add(file2)
root.show()

#component能实现add方法不管是file还是folder类都可以添加，实现了添加文件和文件夹同一个方法

# 这段代码定义了一个 show 方法，用于根据当前层级的缩进（indent）打印文件名，
# 其中 " " * indent 用来生成对应数量的空格，从而在输出时形成层级结构的视觉效果，
# 而 f"File: {self.name}" 则用于显示具体的文件名称。
# 整体作用是在 Composite 模式中，以缩进的方式清晰地展示文件在树状结构中的位置。

##——————————————————————————————————————————————————————————————————————————————————————————————————————

#Observer

#定义一个主体类subject
#__init__(有一个observers的列队和状态state)
# attach（将什么东西加入队列）, detach（将什么东西剔除队列）, set_state（重信设置状态）, notify这几个方法

class Subjcet:
    def __init__(self):
        self._observers = []
        self._state = None
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def set_state(self, state):
        self._state = state
        self.notify()
        #通知所有观察者：状态已经变化，让它们更新
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

#定义Observer抽象类，只有一个update方法供改写
class Observer(ABC):
    def update(self):
        pass

#PhoneDisplay类继承Observer， 重写update
class PhoneDisplay(Observer):
    def update(self,state):
        print(f"Phone display: {state}")
#TVDisplay类继承Observer，重写update
class TVDisplay(Observer):
    def update(self,state):
        print(f"TV display: {state}")


subject = Subjcet()
phone = PhoneDisplay()
TV = TVDisplay()

subject.attach(phone)
subject.attach(TV)

subject.set_state("Temperature: 25")

#这段代码实现了观察者模式，其中 `Subject`（被观察者）维护一个观察者列表，并通过 `attach` 和 `detach` 方法管理观察者；
# 当其内部状态通过 `set_state` 发生变化时，会调用 `notify` 方法遍历所有观察者，
# 并执行它们的 `update` 方法，将最新状态传递给它们。
# 各个具体观察者类实现了 `update` 方法，用于接收并处理状态变化，从而实现对象之间的一对多自动通知机制，降低了对象之间的耦合度。

##——————————————————————————————————————————————————————————————————————————————————————————————————————

#Proxy

#定义一个RealSubject
#__init__, load_from_disk, display
class RealImage:
    def __init__(self,filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading from disk: {self.filename}")
    def display(self):
        print(f"Displaying image: {self.filename}")

#定义代理对象，ProxySubject，

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# Test
image = ProxyImage("photo.jpg")

# 第一次调用（会加载）
image.display()

# 第二次调用（不会重复加载）
image.display()

#在该调用流程中，客户端首先调用代理对象 ProxyImage 的 display() 方法，
#代理会判断真实对象是否已创建；如果未创建，则先实例化 RealImage 并加载资源，然后再调用其方法；
#如果已存在，则直接调用真实对象的方法，从而实现延迟加载并优化性能。
