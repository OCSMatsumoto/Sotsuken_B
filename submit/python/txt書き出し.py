# url="テキストファイルの場所"
url="sample.txt"
#例：url="../Test/cook.txt"　など
f=open(url, "r", encoding="UTF-8")
data=f.readlines()
length=len(data)
for i in range(0,length):
    if i%63==0:
        print("<br>""<br>"+data[i]+"</br>""</br>")
        f = open('sample.html', 'w', encoding='UTF-8')  # 上書き
        f.write("<br>""<br>"+data[i]+"</br>""</br>")
        f.close()
    if i%63!=0:
        while i%63<=62:
            print("<br>""<br>"+data[i]+"</br>""</br>")
            f = open('sample.html', 'a', encoding='UTF-8')  # 追記  
            f.write("<br>""<br>"+data[i]+"</br>""</br>")
            f.close()
            break
f.close()



# f = open('myfile.html', 'w', encoding='UTF-8')

# f.write('こんにちは\n')

# datalist = ['お元気ですか？\n', 'それではまた\n']
# f.writelines(datalist)

# f.close()