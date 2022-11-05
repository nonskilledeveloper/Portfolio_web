from random import randint

# <Random secret key:>
passchars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s',
't','u','v','w','x','y','z'] # 27 chars

passchars_uppers = []
for x in range(len(passchars)):
    passchars_uppers.append(passchars[x].upper())

passnumbers = ['0','1','2','3','4','5','6','7','8','9']

passchars_unusuals = ['#','!',' ','$','/','(',')','=','&','%','°','|','{','}','*',
'[',']','.','_','-',',',';','<','>','¡','¿','?','+'] # 28 chars

pass_order = {
1:passchars,
2:passnumbers,
3:passchars_uppers,
4:passchars_unusuals}

rndscrt_key = ""

for x in range(256):
    temp_char = pass_order[randint(1,4)]
    temp_char = str(temp_char[randint(1, len(temp_char)-1)])
    rndscrt_key = rndscrt_key + temp_char
# </Random secret key>