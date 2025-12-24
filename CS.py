import pandas as pd
import matplotlib.pyplot as plt

data =  {
    'temperature': [22, 23, 21, 24, 25, 23, 22],
'movement': [1,0,1,1,1,0,0,1,1]
}

df= pd.Dataframe(data)
print(df)


plt.figure(figsize=(10,5))

plt.plot (df['temperature'], color='blue')
plt.xlablel('Time')
plt.ylabel('Values')
plt.title('Temperature and Movement Over Time')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df['movement'], color='green')
plt.xlabel('Time')
plt.ylabel('Movement')
plt.title('Movement Over Time')
plt.legend()
plt.show()


sipi = turtle.Turtle()
sipi.shape("turtle")
sipi.color("green")
sipi.forward(100)

tuttle_screen = turtle.Screen()
tuttle_screen.exitonclick()


class LABstudent:
    name: str
    age: int
    major: str

def introduce (self):
    return f"Hi, my name is {self.name}, I am {self.age} years old and I study {self.major}."

John = LABstudent() #object or instance of LABstudent
John.name = "John"
John.age = 32
John.major = "Biology"

Jane = LABstudent()
Jane.name = "Jane"
Jane.age = 25
Jane.major = "Chemistry"

print(John.introduce())
print(Jane.study())

def init__(self, name: str, age: int, major: str):
     self.name = name
     self.age = age
     self.major = major

def introduce(self):
    return f"Hi, my name is {self.name}, I am {self.age} years old and I study {self.major}."

def study(self):
    return f"{self.name} is now studying {self.major}."






