import csv

def opencsv(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close
    return output

def writecsv(filename, a_list):
    f = open(filename, 'w', newline = '')
    csvobject = csv.writer(f, delimiter = ',')
    csvobject.writerows(a_list)
    f.close()

def switch(a_list):
    for i in a_list:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
    return a_list