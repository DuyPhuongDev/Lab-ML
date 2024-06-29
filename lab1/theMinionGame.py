
def minion_game(s):
    anScore=0
    minhScore=0
    vowel = {'U','E','O','A','I'}
    for i in range(len(s)):
        if(s[i] in vowel): 
            minhScore+= (len(s)-i)
        else: 
            anScore+= (len(s)-i)
        
    if(anScore>minhScore): print(f'AN {anScore}')
    elif(anScore<minhScore): print(f'MINH {minhScore}')
    else: print('DRAW')
    
    
s = input('Nhap chuoi s: ')
minion_game(s)