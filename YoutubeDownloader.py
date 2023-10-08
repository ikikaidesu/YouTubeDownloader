# библиотеки
from tkinter import * # графический интерфейс
from tkinter import ttk
from pytube import YouTube # парс ютуб видео
import requests # парс ссылок для изображения
from PIL import Image, ImageTk # для изображений
from io import BytesIO
import tkinter.filedialog as fd
import tkinter.messagebox
def DownloadVideo():
    global video, VideoTitle, EntryName, dir
    if isinstance(dir, str) == False: # проверка установил ли пользователь путь для скачивания
        tkinter.messagebox.showerror("Установщик ютуб видео", "Укажите путь к файлу!")
    elif EntryName.get() == "": # проверка написал ли пользователь название файлу
        tkinter.messagebox.showerror("Установщик ютуб видео", "Укажите название файла!")
    elif ChoiseResolution.get()=="":
        tkinter.messagebox.showerror("Установщик ютуб видео", "Укажите качество файла!")
    else:
        CorrectedName = "".join([i for i in EntryName.get() if i not in '\/:*?"<>|'])
        video.streams.filter(res=ChoiseResolution.get(), type="video")[0].download(output_path=dir, filename=CorrectedName+".mp4")
        tkinter.messagebox.showinfo("Установщик ютуб видео", "Ваше видео успешно скачано в {0}.".format(dir))

# функция для пути к папке куда скачать файл
def dirpath():
    global ChooseLabel, dir
    dir = tkinter.filedialog.askdirectory()
    ChooseLabel.config(text="Видео будет скачано в {0}".format(dir))

# функия с меню для видео
def video():
    global window, LabelVideoTitle, LabelVideoIMG, LabelName, LabelResolution, Resolutions, ChooseLabel, ChoiseResolution, video, VideoTitle, EntryName
    if 'https://www.youtube.com/watch?' not in LinkEntry.get():
        tkinter.messagebox.showerror("Установщик ютуб видео", "Укажите ссылку на ютуб видео!")
    else:
        video = YouTube(LinkEntry.get()) # парсинг видоса
        # вывод названия видео
        VideoTitle = video.title  # название видео
        # делает видео на 2 строки если название длинное
        VideoTitleToLabel = VideoTitle
        if len(VideoTitleToLabel) > 50:
            VideoTitleToLabel = VideoTitleToLabel.split()
            VideoTitleToLabel.insert(len(VideoTitleToLabel) // 2, "\n")
            VideoTitleToLabel = " ".join(VideoTitleToLabel)
        LabelVideoTitle.config(text=VideoTitleToLabel)
        # для вывода превью видео
        VideoIMG = video.thumbnail_url  # превью
        re = requests.get(VideoIMG)
        VideoImage = Image.open(BytesIO(re.content))
        VideoTitleSized = VideoImage.resize((100, 100)) # установка размеров фото
        image = ImageTk.PhotoImage(VideoTitleSized)
        LabelVideoIMG.config(image=image, text='')
        LabelVideoIMG.image = image
        # выбор названия файла
        LabelName.config(text="Название файла ")
        EntryName = Entry(window, width=50)
        EntryName.place(x=250, y=283)
        LabelResolution.config(text="Разрешение")
        ChoiseResolution = ttk.Combobox(values=Resolutions)
        ChoiseResolution.place(x=250, y=325)
        ChooseButton = Button(window, text="Выбрать папку", command=dirpath, width=12, height=1, font=("Arial Bold", 12))
        ChooseButton.place(x=105, y=375)
        DownloadButton = Button(window, text="Скачать", command=DownloadVideo, width=12, height=1, font=("Arial Bold", 12))
        DownloadButton.place(x=250, y=375)


# окно
window = Tk()  # создание окна
window.title("Ютуб установщик")  # титульное название программы
window.geometry('700x600+350+200')  # размеры окна
window.iconbitmap('icon.ico')  # иконка
window.resizable(width=False, height=False) # запрет на изменение разрешения окна
Frame(window, bg="#2b2929", width=700, height=600).place(x=0, y=0) # задний фон

# интерфейс
info = Label(window, text="Установщик ютуб видео", font=("Arial Bold", 24), bg="#2b2929", fg="white") # информация
info.place(x=180, y=20)
Link = Label(window, text="Ссылка на видео", bg="#2b2929", fg="white", font=("Arial Bold", 14))
Link.place(x=30, y=80)
LinkEntry = Entry(window, width=70)
LinkEntry.place(x=190, y=87)
LinkButton = Button(window, text="загрузить",command=video,  width=8, height=1, font=("Arial Bold", 14), bg="#B41C1C", fg="white")
LinkButton.place(x=300, y=120)

# о видео
LabelVideoTitle = Label(window, text="", bg="#2b2929", fg="white", anchor=W)
LabelVideoTitle.place(x=250, y=200)
LabelVideoIMG = Label(window, bg="#2b2929")
LabelVideoIMG.place(x=110, y=160)
LabelName = Label(window, bg="#2b2929", fg="white", font=("Arial Bold", 12))
LabelName.place(x=105, y=280)
LabelResolution = Label(window, bg="#2b2929", fg="white", font=("Arial Bold", 12))
LabelResolution.place(x=105, y=320)
Resolutions = ["360p", "720p", "1080p"]
ChooseLabel = Label(window, text="", font=("Arial Bold", 10), bg="#2b2929", fg="white")
ChooseLabel.place(x=150, y=420)

window.mainloop() # запуск окна