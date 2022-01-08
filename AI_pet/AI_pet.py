from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time
import shutil
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import sounddevice as sd
from scipy.io.wavfile import write
from emotion_model import emo_detect


global ifchangepic
ifchangepic = 0
prev_mood = 'Neutral'
curr_gif = 0

global emo_resp
emo_resp = "???"

def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1000)
        for r in range(rows):
            trg.rowconfigure(r, weight=1000)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

def bt1_event():
    fs = 44100 # Sample rate
    seconds = 3 # Duration of recording
    myrecording = sd.rec(int(seconds * fs),samplerate=fs,channels=2)
    sd.wait() # Wait until recording is finished
    write('audio_recording.wav',fs,myrecording) # Save as WAV file
    source = r'audio_recording.wav'
    destination = r'emotion_model\input_data'
    shutil.copy(source, destination)
    global ifchangepic
    ifchangepic = 1

def layer2(prev_mood, curr_gif):
    #return what layer2 output @@@
    emo, num = emo_detect.detect(prev_mood, curr_gif)
    print(emo, num)
    return emo, num


window = tk.Tk()
window.title('AI PET')
align_mode = 'nswe'
pad = 5

div_size = 200
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='blue')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='orange')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='red')
div4 = tk.Frame(window,  width=div_size , height=div_size , bg='green')

window.update()
win_size = min( window.winfo_width(), window.winfo_height())
print(win_size)

div1.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
div2.grid(column=0, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=0, row=3, padx=pad, pady=pad, sticky=align_mode)
div4.grid(column=0, row=2, padx=pad, pady=pad, sticky=align_mode)

define_layout(window, cols=1, rows=4)
define_layout([div1, div2, div3, div4])


lbl_title1 = tk.Label(div2, text='Hello I am your lovely pet!', bg='orange', fg='white')
lbl_title2 = tk.Label(div2, text="I will always listen to you", bg='orange', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)


resp_title1 = tk.Label(div4, text='oh you heard so', bg='green', fg='white')
text = tk.StringVar()
text.set('???')
resp_title2 = tk.Label(div4, textvariable=text, bg='green', fg='white')

resp_title1.grid(column=0, row=0, sticky=align_mode)
resp_title2.grid(column=0, row=1, sticky=align_mode)


bt1 = tk.Button(div3, text='say somethin to me', bg='red', fg='white')
bt1.grid(sticky=align_mode)
bt1['command'] = bt1_event

define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=1)
define_layout(div4, rows=2)


#run gif
global a,flag
im = Image.open('./gifs/004.gif')   
while 1:
    # GIF iterator
    iter = ImageSequence.Iterator(im)
    #frame就是gif的每一帧，转换一下格式就能显示了
    for frame in iter:
        pic=ImageTk.PhotoImage(frame)
        image_main = tk.Label(div1, image=pic)
        image_main['height'] = img_size
        image_main['width'] = img_size

        image_main.grid(column=0, row=0, sticky=align_mode)
        time.sleep(0.1)
        window.update_idletasks()  #刷新
        window.update()

    if(ifchangepic):
        emo, pic_change = layer2(prev_mood, curr_gif)
        pic_change_str = str(pic_change+1).zfill(3)
        im = Image.open('./gifs/'+pic_change_str+'.gif')
        ifchangepic = 0
        print("hi")
        prev_mood = emo
        curr_gif = pic_change
        emo_resp = emo
        text.set(emo_resp)
        

    #window.mainloop()




#im = Image.open('./gifs/003.gif')
#imTK = ImageTk.PhotoImage( im.resize( (img_size, img_size) ) )
#image_main = tk.Label(div1, image=imTK)
#image_main['height'] = img_size
#image_main['width'] = img_size

#image_main.grid(column=0, row=0, sticky=align_mode)

"""
def pick(event):
    global a,flag   
    while 1:
        im = Image.open('./gifs/003.gif')
        # GIF图片流的迭代器
        iter = ImageSequence.Iterator(im.resize(img_size, img_size))
        #frame就是gif的每一帧，转换一下格式就能显示了
        for frame in iter:
            pic=ImageTk.PhotoImage(frame)
            image_main = tk.Label(div1, image=pic)
            image_main['height'] = img_size
            image_main['width'] = img_size

            image_main.grid(column=0, row=0, sticky=align_mode)
            time.sleep(0.1)
            window.update_idletasks()  #刷新
            window.update()

            #canvas.create_image((100,150), image=pic)
            #time.sleep(0.1)
            #root.update_idletasks()  #刷新
            #root.update()

div1.bind("<Enter>",pick)  #这个事件是鼠标进入组件，用什么事件不重要，这里只是演示

"""


"""
im = Image.open('./gifs/003.gif')
# GIF图片流的迭代器
iter = ImageSequence.Iterator(im)
#frame就是gif的每一帧，转换一下格式就能显示了
for frame in iter:
    pic=ImageTk.PhotoImage(frame)
    image_main = tk.Label(div1, image=pic)
    image_main['height'] = img_size
    image_main['width'] = img_size

    image_main.grid(column=0, row=0, sticky=align_mode)
    time.sleep(0.1)
    window.update_idletasks()  #刷新
    window.update()

window.mainloop()
"""



"""
lbl_title1 = tk.Label(div2, text='Hello', bg='orange', fg='white')
lbl_title2 = tk.Label(div2, text="World", bg='orange', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

bt1 = tk.Button(div3, text='Record', bg='red', fg='white')

bt1.grid(column=0, row=0, sticky=align_mode)

bt1['command'] = bt1_event

define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=4)

window.mainloop()

"""