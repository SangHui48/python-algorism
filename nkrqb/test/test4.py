with open('./resource/a.txt','r') as f:
    print(f.readline())
    
try:
    f.readline()
except:
    print('aaa')