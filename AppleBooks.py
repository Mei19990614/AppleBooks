

title=input('请输入标题：')
note_path='/Users/meiouyang/Desktop/%s.txt'%title
save_path='/Users/meiouyang/Desktop/Kindle/'
# find_date=re.compile(r'(\d{4})年(\d{1,2})月(d{1,2})日',re.S)

f=open(note_path,'r+')

note=[]
for i in range(0,10000):
    line=f.readline()
    #print(line)
    if not line:
        break
    if line!='\n':
        note.append(line)
# print(len(note))
# print(note[6])

basenote=note[8:len(note)-3]
# print(basenote)

trim_note=[]
for i in range(0,len(basenote)//3):
    chunk=basenote[i*3+1:i*3+3]
    trim_note.append(chunk)

book_note=open('%s%s.txt'%(save_path,str(note[6])),'a+')
book_note.write(trim_note[0][0])
char=trim_note[0][0]
for i in range(0,len(trim_note)):
    book_note.write(trim_note[i][1])
    #print(trim_note[i][1])
    if trim_note[i][0]!=char:
        book_note.write('\n')
        book_note.write(trim_note[i][0])
        # print(trim_note[i][0])
        char=trim_note[i][0]

book_note.close()

f.close()

print('完成！')