from readings import test, OUTPUT_FILE
import math

def load_file(filename):
    loc_data = []
    with open(OUTPUT_FILE, "r") as f:
        for line in f:
            data = eval(line)   
            loc_data.append(data)
    return loc_data

  
    
def rms_num(signal1, signal2):
    #ds1 = dict(signal1)
    #ds2 = dict(signal2)
    flag1 = 0
    flag2 = 0
    s1 = 0
    s2 = 0
    l = len(signal1)
    m = len(signal2)
    if l > m:
        t = l
        l = m
        m = l
    for i in range(0,l):
            if signal1[i][0] == signal2[i][0]:
                flag1 = flag1 + 1
                s1 += (signal1[i][1] - signal2[i][1])**2
            else:
                continue
    for i in range(0,l):
            if signal1[i][0] != signal2[i][0]:
                for j in range(0,len(signal2)):
                    if signal1[i][0] == signal2[j][0]:
                        flag2 = flag2 + 1
                        s2 += (signal1[i][1] - signal2[i][1])**2
            else: 
                continue
    if flag1 >= 3: 
        return s1
        #return s
    elif flag2 >= 5:
        return s2 
    else:
        return 0  
        
def find_best_match(cur_signal):
    locs = load_file(OUTPUT_FILE)
    f = 0
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    l = "'CEEMS-LAB'"
    k = "'IIIT-B-Xerox'"
    m = "'CLASS_ROOM-132'"
    q = "'linksys_SES_13598'"
    for n in cur_signal:
        if n[0] == l:
            f = 1
    for n in cur_signal:
        if n[0] == k:
            f1 = 1    
    for n in cur_signal:
        if n[0] == m:
            f3 = 1
    for n in cur_signal:
        if n[0] == q:
            f4 = 1
    if f == 0:        
        return -1
    if f3 != 0:
        if f == 1 and f1 == 1:
           for n in cur_signal:
              if n[0] == k and n[1] < 40:
                 f2 = 1       
        if f == 1 and f1 == 0:
            for n in cur_signal:
                if n[0] == l and n[1] > 10:
                    f2 = 1 
        if f2 == 0:
            return -1
        if f == 1 and f1 == 1 and f4 == 1:
            for n in cur_signal:
                if n[0] == q and n[1] > 25:
                    return -1 
                    
         

    rms_nums = map(lambda x: (x[0], rms_num(cur_signal, x[1])),
                   locs)
    rms_nums.sort(key=lambda x: x[1])
    for r in range(0,len(rms_nums)):
        if rms_nums[r][1] != 0:
            return rms_nums[r][0]
        else:
            continue
            
       

if __name__ == "__main__":
    avgs = test()
    best = find_best_match(avgs)
    if best == -1:
        print "Location unknown, maybe the ground floor, please ask a human for help!"
    else:
        best = best.replace("_", " ")
        best = best.replace("-", " ")
        #print "Nearest known location is:", best
        print best
