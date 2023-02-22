import pandas as pd
def convertToInt(myStr):
    myStrInt=[ord(c) for c in myStr]
    return myStrInt
# print (convertToInt("Haithem"))
def xor(a, b):
    return a ^ b
def generator(k):
    if (len(k)<5 or len(k)>256):
        print ("you need to write key between 5 and 256")
        return 
    S=[]
    for i in range(0,256):
        S.append(i)
        # print (S[i])
    j=0
    key=convertToInt(k)
    for i in range(0,256):
        j=(j+S[i]+key[i % len(key)])% 256
        S [i],S[j] =S[j],S[i]
    return S

# print (len(generator(k="Haithem")))
cle=generator(k="haithem")
mess="Bonjour"
# print (convertToInt(mess))
def convertMessage(cle ,mess):
    i=0
    j=0
    EncMess=[]
    S=generator(cle)
    messInt=convertToInt(mess)
    print ("message int ",messInt)
    print ("mess len ",len(messInt))
    for charMess in messInt:
        i=(i + 1)% 256
        j=(j + S[i])%256
        S[i] , S[j] = S[j] ,S[i]
        octecChif = S[ ( S[i] + S[j] ) % 256]

        # print ("octet chiff ",octecChif)
        # print ("index i",i)
        # print ("the message Int", charMess)
        result = octecChif ^ charMess
        EncMess.append(result)
    arrChar=[]
    str=""
    for m in EncMess:
        arrChar.append(chr(m))
    str=''.join(arrChar)
    return str

        


arr=convertMessage("haithem","Ahla")

print ("the last one ",arr)

print ("the dechiffrement is ",convertMessage("haithem",arr))









         