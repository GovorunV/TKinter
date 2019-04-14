import tkinter as tk# импорт библиотеки для прилежений
from tkinter import ttk #импорт для инструментов(батон,лейбел...)
from tkinter import * #импортируем все
import webbrowser #импорт работы с браузером
def search(): #функция для поиска
    if text_field.get().strip() != "":
        if search_eng.get() == "google":
            webbrowser.open('https://www.google.com/search?q=' + text_field.get()) #склеюем строки(через get получаем значение)
        elif search_eng.get() == "bing":
            webbrowser.open('https://www.bing.com/search?q=' + text_field.get())  # склеюем строки(через get получаем значение)
def search1():
    search()
def enterBut(event):#функция для поиска через ентер
    search()

app=tk.Tk() #создаем приложение
search_eng = StringVar() #переменая
search_eng.set("google") #установить по умолчанию (set-установить значение)
app.title("Find system") #название окна
#Надпись
search_lable = ttk.Label(app, text = "Приложение для поиска", font='verdana 15 bold italic', foreground='red') #шрифт verdana 15размер наклоненый(italic),цвет красный(можно через #333) жирный(bolt)
search_lable.grid(row=0, column=1) # присваимываем позицию 0 0(слева сверху)
#Надпись
search_lable = ttk.Label(app, text = "Поиск") #создаем надпись
search_lable.grid(row=1, column=0) # присваимываем позицию 0 0(слева сверху)
#Поле для ввода текста
text_field = ttk.Entry(app, width=50) # создаем поле для ввода
text_field.grid(row=1, column=1) #присваиваем позицию 0 1(немного правее от надписи)
#Кнопка поиска
buton_search=ttk.Button(app, text="Найти", width=10, command=search1)
buton_search.grid(row=1, column=2) #
#Radio button
radio_google=ttk.Radiobutton(app, text="Google", value="google", variable=search_eng) #записывает значение google в переменую search_eng
radio_google.grid(row=2, column=1 , sticky=W) # sticky W это немного левее
radio_bing=ttk.Radiobutton(app, text="Bing", value="bing", variable=search_eng)#записывает значение bing в переменую search_eng
radio_bing.grid(row=2, column=1 , sticky=E) # sticky E это немного правее

text_field.bind('<Return>', enterBut) #функция бин должна принемать аргемент(поэтому создаем еще одну функцию для обработки ентр)


text_field.focus() #установка активного поля( тоесть сразу будет активная строка)
app.wm_attributes('-topmost', True)
app.mainloop() #зациклюем прогу