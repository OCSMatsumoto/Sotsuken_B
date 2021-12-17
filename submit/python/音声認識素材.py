import wave
import struct
from scipy import fromstring,int16
import numpy as np
import os
import math
import speech_recognition as sr
import pandas as pd
import tkinter.filedialog
from itertools import count

xxx = 0


#filenameに読み込むファイル、timeにカットする間隔
def cut_wav(filename,time):  
    

    # ファイルを読み出し
    wavf = filename
    wr = wave.open(wavf, 'r')


    ch = wr.getnchannels()
    width = wr.getsampwidth()
    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr 
    integer = math.floor(total_time*100) 
    t = int(time*100)  
    frames = int(ch * fr * t /100)
    num_cut = int(integer//t)
    
    data = wr.readframes(wr.getnframes())
    wr.close()
    X = np.frombuffer(data, dtype=int16)

    for i in range(num_cut + 1):
        # 出力データを生成
        outf = out_dir + '/' + str(i) + '.wav' 
        # 音声をカットした部分は少し巻き戻す
        if i > 0:
            start_cut = int(i*frames) - int(180000)
        else:
            start_cut = int(i*frames)

        end_cut = int(i*frames + frames)
        # print(start_cut)
        # print(end_cut)
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        # 書き出し
        ww = wave.open(outf, 'w')
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()

    str_out = ""
    list1 = [wavf,"",""]
    df_x = pd.DataFrame([list1])
    df_x.columns = ['No', '音声ファイル', '変換結果']

    for ii in range(num_cut + 1):
        outf = out_dir + '/' + str(ii) + '.wav' 
        str_out = wav_to_text(outf)
        df_x.loc[ii] = [ii,str(ii) + '.wav',str_out]

    # excelへ書き出し
    with pd.ExcelWriter(out_file) as writer:
        df_x.to_excel(writer, sheet_name='結果', index=False)
      	    
    

def wav_to_text(wavfile):
    global xxx
    r = sr.Recognizer()

    with sr.AudioFile(wavfile) as source:
        audio = r.record(source)

    wav_to_text = r.recognize_google(audio, language='ja-JP')

    print(wav_to_text)

    # .txt作成
    if xxx > 0:
        # print("<br>"+wav_to_text+"</br>")
        f = open('sample.txt', 'a', encoding='UTF-8')  # 作成
        f.write(wav_to_text +'\n')
        f.close()
        xxx+=1

    if xxx == 0:
        # print("<br>"+wav_to_text+"</br>")
        f = open('sample.txt', 'w', encoding='UTF-8')  # 上書き
        f.write(wav_to_text +'\n')
        f.close()
        xxx = xxx + 1

    

    return wav_to_text


out_dir = "output"
file = os.path.exists(out_dir)
# print(file)

if file == False:
    #保存先のディレクトリの作成
    os.mkdir(out_dir)

fTyp = [("","*.wav")]
iDir = os.path.abspath(os.path.dirname(__file__))
f_name = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

cut_time = 60

# excelファイルの重複判定

# エクセルファイル作成プログラム
#ファイルが存在しないとき"output1.xlsx"を作成"
# 存在しているときは"output2.xlsx"を作成
# それも存在しているときは"output3.xlsx"を作成 
#以下同文

file_path = "output/out{}.xlsx"
out_file = ""
for num in count(1):
    if not os.path.exists(file_path.format(num)):
        out_file = file_path.format(num)
        break

    out_file = "output/out1.xlsx"

# if(os.path.exists("output/out1.xlsx") == True):

#     if(os.path.exists("output/out2.xlsx") == True):

#         if(os.path.exists("output/out3.xlsx") == True):

#             if(os.path.exists("output/out4.xlsx") == True):

#                 if(os.path.exists("output/out5.xlsx") == True):

#                     out_file = "output/out6.xlsx"
#                 else:
#                     out_file = "output/out5.xlsx"
#             else:
#                 out_file = "output/out4.xlsx"
#         else:
#             out_file = "output/out3.xlsx"
#     else:
#         out_file = "output/out2.xlsx"
# else:

cut_wav(f_name,float(cut_time))