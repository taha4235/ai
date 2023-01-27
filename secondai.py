import pyttsx3
import speech_recognition as sr
import webbrowser
import time
wel=pyttsx3.init()
voices=wel.getProperty('voices')
wel.setProperty('voices',voices[0].id)
def speak(audio):
    wel.say(audio)
    wel.runAndWait()
def takecommands():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
      print('say your commands sir')
      command.phrase_threshold=1
      audio=command.listen(mic)
      try:
        print('recordigs......')
        query=command.recognize_google(audio,language='en')
        print(f'you said :{query}')
      except Exception as Error:
        return None
      return query.lower()
speak('hello sir taha how are you today how ican help you')
while True:
    query=takecommands()
    if 'good morning' in query:
      speak('hello dears good morning')
    if 'hello' in query:
        speak('hello how are you iam fine and you')
    if 'open to me google' in query:
        speak('for sure dears taha i will open to you google')
        webbrowser.open_new_tab('https://www.google.com')
    if 'how old are you robot' in query:
      speak('i dont have an age beacause iam a robot just to make a ai appliaction')
    if 'open to me youtube' in query:
      speak('you want to watch an action movies')
      time.sleep(2)
    if 'yes i want  to watch an action movies' in query:
      webbrowser.open_new_tab('https://www.youtube.com')
    if 'do i have any date' in query:
      speak('yes taha you have a date at 9:00pm for make a python application')
    if 'do i have any applications tommorow' in query:
      speak('yes you have somethings to do it')
    if 'where are you from ' in query:
      speak('am from lebanon')
      time.sleep(2)
    if 'open my facebook' in query:
      speak('for sure i will open to your facebook')
      time.sleep(1)
      webbrowser.open_new_tab('https://www.facebook.com')
    if 'whats your opinion about chatgpt' in query:
      speak('chat gpt is one of the most succesfull aplication used around the world and it help me alot in my projects')
    if 'what do you want to do tomorrow' in query:
      speak('i will make some projects like web template and gui applications and i will do somethings like python script')
    if 'make to me a web application' in query:
      speak('for sure dears here an example about we application using pywebio library')
      import pywebio
      from pywebio.output import *
      from pywebio.input import *
      from pywebio.pin import *
      from pywebio import start_server
      from pywebio.session import *
      name=input(
        type='name',
        placeholder='your name',
        name='name',
      )
      lastname=input(
        type='text',
        placeholder='last name',
        name='last name',
      )
      email=input(
        type='text',
        placeholder='email',
        name='email',
      )
      password=input(
        type='password',
        placeholder='password',
        name='password',
      )
      put_text('your name is:%r'%name)
      put_text('your name is:%r'%lastname)
      put_text('your name is:%r'%email)
      put_text('your name is:%r'%password)
    if ' calculator' in query:
      speak('for sure dears here is a simple example using python')
      def calcuator():
        operation = input("What operation would you like to perform (+, -, *, /): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
          print(num1 - num2)
        elif operation == '*':
          print(num1 * num2)
        elif operation == '/':
          print(num1 / num2)
        else:
          print("Invalid operator")

        calcuator()
    if 'application ' in query:
      speak('for sure dears here is a simple tkinter application')
      import tkinter as tk
      root =tk()
      root.title('simple tkinter applications using python')
      root.geometry('200x200')
      root.mainloop()
    if 'login to my faceook account' in query:
      speak('for sure i will do that wait a couples of seconds')
      from selenium import webdriver
      from getpass import getpass
      driver = webdriver.Edge()
      driver.get('https://www.facebook.com')
      username=input('enter your email here:')
      pasword=getpass('enter your face password:')
      textusername=driver.find_element_by_id('email')
      textusername.send_keys(username)
      textpassword=driver.find_element_by_id('pass')
      textpassword.send_keys(pasword)
      btnlogin=driver.find_element_by_id('u_0_b')
      btnlogin.submit()
    if 'open github' in query:
      speak('you want to open your own account')
    if 'yes open it' in query:
      webbrowser.open_new_tab('https://www.github.com')
      time.sleep(2)
    if 'what do you want to do tomorrow' in query:
      speak('i will work in some projects like web template and some javascript and java code and thats it')
    



