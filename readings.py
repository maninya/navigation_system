from subprocess import Popen, PIPE
import time
import sys

OUTPUT_FILE = "final_readings.txt"

def replace_s_with_u(line):
    seps = line.split("'")
    if seps[0] == "" and len(seps) == 3:
        seps[1] = seps[1].replace(" ", "_")
        return "'%s'%s" % (seps[1], seps[2])
    elif seps[0] == "" and len(seps) == 4:
        seps[1] = seps[1].replace(" ", "_")
        seps[2] = seps[1].replace(" ", "_")
        return "'%s %s'%s" % (seps[1], seps[2], seps[3])
    return line

def readsignals():
    p = Popen("LC_ALL=C nmcli -f SSID,SIGNAL dev wifi list",
              shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0].strip()

    lines = output.split("\n")[1:]
    sig_dict = {}
    for line in lines:
        #now replace spaces inside quoted substrings with underscore
        line = replace_s_with_u(line)
        #beautify
        line = line.split()
        sig_dict[line[0]] = int(line[1])
    return sig_dict

def do_experiment(interval=2):
    r = []
    for i in range(0,17):
        r.append(readsignals())
        time.sleep(interval)
    avgs = {}
    for i in r:
        for w in i.keys():
            avgs[w] = i[w]
            for j in r:
                if j != i:
                    if w in j.keys():
                        avgs[w] += j[w]
            avgs[w] = avgs[w]/17              
                          
    avg_sigs = list(avgs.items())
    #sort descending
    avg_sigs.sort(key=lambda x: x[1], reverse=True) 
    return avg_sigs#[:3] 
    
def test():
    r = readsignals()
    #time.sleep(interval)                      
    avg_sigs = list(r.items())
    #sort descending
    avg_sigs.sort(key=lambda x: x[1], reverse=True) 
    return avg_sigs#[:3]
    
def write_output(name, signals):
    output = (name, signals)
    with open(OUTPUT_FILE, "a+") as f:
        f.write(repr(output) + "\n")

if __name__ == "__main__":
    print "Doing experiment: ..."
    avgs = do_experiment()
    loc = sys.argv[1]
    print "done!"
    write_output(loc, avgs)
    print "Wrote output."

