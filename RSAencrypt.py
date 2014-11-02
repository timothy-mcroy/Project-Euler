def encrypt(x,e,modu):
    return (x**e)%modu
def letterValue(character):
    if( ord(character)-97 >9):
        return str(ord(character)-97)
    else:
        return ('0'+str(ord(character)-97))
def valueLetter(IntegerString):
    return chr(IntegerString%26+97)
def EuAg(Big, Small):
        if (Big%Small==0):
                return Small
        else:
                return EuAg(Small, Big%Small)
def RSA(Unencrypted, e, p,q):
    assert (len(Unencrypted)%2 == 0)
    Unencrypted=list(Unencrypted)
    i=0
    Accum=[]
    g=p*q
    while(i<len(Unencrypted)):
        x=Unencrypted[i]
        y=Unencrypted[i+1]
        x=letterValue(x)
        y=letterValue(y)
        Block = int(x+y)
        EncryptedBlock= str(encrypt(Block, e, g))
        print (EncryptedBlock)
        if (len(EncryptedBlock)<4):
            Accum.append("0"+EncryptedBlock)
        else:
            Accum.append(EncryptedBlock)


        
        i+=2
    return Accum
def Decrypt(Encrypted, d, p, q):
    '''Not working properly'''
    Accum= []
    for element in Encrypted:
        element=str(encrypt(int(element), d, (p-1)*(q-1)))
        #Accum+=element
        if (len(element)<4):
            a=int(element[0])
            b=int(element[1::])
        else:
            a=int(element[:2])
            b=int(element[2::])
        g=str(valueLetter(a))+str(valueLetter(b))
        Accum+=g
        
    return Accum

        
    
    
