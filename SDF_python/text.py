import time 

def sample (x:int ,y:int ) -> str:

    if(x+y+int(time.time()))%4:
        return '#'
    else:
        return'*'
while True:
        format_chars = []
        for y in range(20):
            for x in range(80):
                format_chars.append(sample(x,y))
            format_chars.append('\n')
        print(''.join(format_chars))
        time.sleep(1/30)