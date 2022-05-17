
# Create your views here.
import time,datetime
import subprocess
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from more_itertools import value_chain
import time,datetime
import hashlib
import array
import random
import pandas
#import leveldb




class CMSketch(object):
    def __init__(self, m, d):
        """ `m` is the size of the hash tables, larger implies smaller
        overestimation. `d` the amount of hash tables, larger implies lower
        probability of overestimation.
        """
        if not m or not d:
            raise ValueError("Table size (m) and amount of hash functions (d)"
                             " must be non-zero")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        for _ in range(d):
            table = array.array("l", (0 for _ in range(m)))
            self.tables.append(table)

    def _hash(self, x):
        md5 = hashlib.md5(x)
        for i in range(self.d):
            md5.update(str(i).encode("utf-8"))
            yield int(md5.hexdigest(), 16) % self.m

    def add(self, x, value):
        """
        Count element `x` as if had appeared `value` times.
        By default `value=1` so:
            sketch.add(x)
        Effectively counts `x` as occurring once.
        """
        self.n += value
        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
            table[i] = table[i] + value

    def query(self, x):
        """
        Return an estimation of the amount of times `x` has ocurred.
        The returned value always overestimates the real value.
        """
        return min(table[i] for table, i in zip(self.tables, self._hash(x.encode("utf-8"))))

def positive_or_negative():
        if random.random() < 0.5:
            return 1
        else:
            return -1
def get_median(data):
    data = sorted(data)
    size = len(data)
    if size % 2 == 0: # 判断列表长度为偶数
        median = (data[size//2]+data[size//2-1])/2
        data[0] = median
    if size % 2 == 1: # 判断列表长度为奇数
        median = data[(size-1)//2]
        data[0] = median
    return data[0]


class CSketch(object):
    
    
    def __init__(self, m, d):
        """ `m` is the size of the hash tables, larger implies smaller
        overestimation. `d` the amount of hash tables, larger implies lower
        probability of overestimation.
        """
        if not m or not d:
            raise ValueError("Table size (m) and amount of hash functions (d)"
                             " must be non-zero")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        for _ in range(d):
            table = array.array("l", (0 for _ in range(m)))
            self.tables.append(table)

    def _hash(self, x):
        md5 = hashlib.md5(x)
        for i in range(self.d):
            md5.update(str(i).encode("utf-8"))
            yield int(md5.hexdigest(), 16) % self.m
            
    def add(self, x, value=1):
        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
            table[i] = table[i] + positive_or_negative() * value

    def query(self, x):
        """
        Return an estimation of the amount of times `x` has ocurred.
        The returned value always overestimates the real value.
        """
        list_ = []
        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
            list_.append(table[i]*positive_or_negative())       
        return get_median(list_)

def get_median(data):
    data = sorted(data)
    size = len(data)
    if size % 2 == 0: # 判断列表长度为偶数
        median = (data[size//2]+data[size//2-1])/2
        data[0] = median
    if size % 2 == 1: # 判断列表长度为奇数
        median = data[(size-1)//2]
        data[0] = median
    return data[0]


class CMMSketch(object):


    def __init__(self, m, d):
        """ `m` is the size of the hash tables, larger implies smaller
        overestimation. `d` the amount of hash tables, larger implies lower
        probability of overestimation.
        """
        if not m or not d:
            raise ValueError("Table size (m) and amount of hash functions (d)"
                             " must be non-zero")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        for _ in range(d):
            table = array.array("l", (0 for _ in range(m)))
            self.tables.append(table)

    def _hash(self, x):
        md5 = hashlib.md5(x)
        for i in range(self.d):
            md5.update(str(i).encode("utf-8"))
            yield int(md5.hexdigest(), 16) % self.m

    
    def add(self, x, value):
        """
        Count element `x` as if had appeared `value` times.
        By default `value=1` so:
            sketch.add(x)
        Effectively counts `x` as occurring once.
        """
        self.n = self.n + 1
        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
            table[i] = table[i] + value        
#        list_ = []
#        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
#            list_.append(table[i])
#            min1 = min(list_)
#        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
#            table[i]=max(min1+value,table[i])

    def query(self, x):
        """
        Return an estimation of the amount of times `x` has ocurred.
        The returned value always overestimates the real value.
        """   
        
#        estimate1 = min(table[i] for table, i in zip(self.tables, self._hash(x.encode("utf-8"))))
#        estimate2 = 
        return get_median(table[i]-(self.n-table[i])/(max(self.m-1,1)) for table, i in zip(self.tables, self._hash(x.encode("utf-8"))))

class CMCUSketch(object):

    def __init__(self, m, d):
   
        if not m or not d:
            raise ValueError("Table size (m) and amount of hash functions (d)"
                             " must be non-zero")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        for _ in range(d):
            table = array.array("l", (0 for _ in range(m)))
            self.tables.append(table)

    def _hash(self, x):
        md5 = hashlib.md5(x)
        for i in range(self.d):
            md5.update(str(i).encode("utf-8"))
            yield int(md5.hexdigest(), 16) % self.m

    
    def add(self, x, value):
        """
        Count element `x` as if had appeared `value` times.
        By default `value=1` so:
            sketch.add(x)
        Effectively counts `x` as occurring once.
        """
        list_ = []
        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
            list_.append(table[i])
        min1 = min(list_)
        for table, i in zip(self.tables, self._hash(x.encode("utf-8"))):
            table[i]=max(min1+value,table[i])

    def query(self, x):
        """
        Return an estimation of the amount of times `x` has ocurred.
        The returned value always overestimates the real value.
        """
        return min(table[i] for table, i in zip(self.tables, self._hash(x.encode("utf-8"))))   

def home(request):
    return render(request, 'index.html')


def sketch(request):
    return render(request, 'sketch.html')

def run_code(code):
    try:
        code = 'print('+ code + ')'
        output = subprocess.check_output(['python','-c',code],
                                         universal_newlines=True,
                                         stderr = subprocess.STDOUT,
                                         timeout = 30)
    except subprocess.CalledProcessError as e:
        output = '公式输入有hkjhjkj误'
    return output

@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    print(result)
    return JsonResponse(data={'result': result})


@csrf_exempt
@require_POST
def compute2(request):
    value1 = request.POST.get('value1')

    print("value1:"+value1)
    value2 = request.POST.get('value2')
    result = run_code(value1)
    result = '7'
    print("result:"+result)
    print("op"+value1+" "+value2+" "+result)
    return JsonResponse(data={'result': result})

@csrf_exempt
@require_POST
def sketchCompute(request):
    value1 = request.POST.get('data_begin')
    value2 = request.POST.get('data_end')
    value3 = request.POST.get('sketch_choice')
    query1 = request.POST.get('query1')
    query2 = request.POST.get('query2')
    query3 = request.POST.get('query3')
    query4 = request.POST.get('query4')
    query5 = request.POST.get('query5')


    #  print("value1:"+value1)
    #  print("value2:"+value2)
    #  print("value3:"+value3)
    #  print("value4:"+value4)
    if value3 == "CMSketch":
        sketch = CMSketch(5000,2)
    elif value3 == "CMMSketch":
        sketch = CMMSketch(5000,2)
    elif value3 == "CSketch":
        sketch = CSketch(5000,2)
    elif value3 == "CMCUSketch":
        sketch = CMCUSketch(5000,2)

     #sketch_choice = request.POST.get('sketch_choice')
    time1=datetime.datetime.strptime(value1,"%Y-%m-%dT%H:%M:%S")
    time2=datetime.datetime.strptime(value2,"%Y-%m-%dT%H:%M:%S")
    secondsFrom1970_1=time.mktime(time1.timetuple())    
    secondsFrom1970_2=time.mktime(time2.timetuple())   #读入查询时间
    print(secondsFrom1970_2)
    print(secondsFrom1970_1)

    db = leveldb.LevelDB("./dbtest900")
    for key,value in db.RangeIter():
        value = value.decode().split("@")
    #print(len(value.split("@")))
        length = len(value)
        for i in range(length):
            value[i] = value[i].split(" ")
            if float(value[i][0])>secondsFrom1970_1 and float(value[i][0])<secondsFrom1970_2:
                sketch.add(key,1)


    # with open(r"C:\Users\11420\Desktop\computer-master\app\pcap.txt",'r') as f:
    #     all_data = f.readlines()
    #     for i in range(len(all_data)):
    #         line = all_data[i].split(" ")
    #         time_1 = float(line[0])
    #         print("\n")
    #         if time_1>secondsFrom1970_1 and time_1<secondsFrom1970_2:
    #             #strin = print(line[6],line[8],line[9],line[10],line[11])
    #             strin = str(line[6]+" "+line[8]+" "+line[9]+" "+line[10]+" "+line[11])
    #             print(strin)
    #             sketch.add(strin,1)
    #         else: break
    #query = sketch.query(str(query1)+" "+str(query2)+" "+str(query3)+" "+str(query4)+" "+str(query5))
    query = sketch.query(str(query1)+""+str(query2)+""+str(query3)+""+str(query4)+""+str(query5))
    #print("query:", query)
    #print("query:",str(query1)+""+str(query2)+""+str(query3)+""+str(query4)+""+str(query5), query)
     
    #  sketch.add("1",1)
    #  sketch.add("1",1)
    #  sketch.add("1",1)
    #  query = sketch.query("1")
    return JsonResponse(data={'result1': query})