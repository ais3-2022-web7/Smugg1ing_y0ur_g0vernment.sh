#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import numpy as np
from tqdm import trange
import sys
import time
import timeout_decorator
from pathlib import Path
### functions
def scanurl (url):
    reurl = r'curl -sIL -w "%{http_code}\n" -o /dev/null ' + "" + url
    result = os.popen(reurl)
    context = result.read()
    state = ""
    for line in context.splitlines():
        state += line
    result.close()
    return(state)

def _handle_timeout(signum, frame):
    raise TimeoutError('function timeout')


@timeout_decorator.timeout(int(sys.argv[2]))
def test(url):
    if sys.argv[1] == '--timeout':
            meow = scanurl(url)
            print(meow,end="<===")
            print(url)
            if meow != '000' and meow != '404' : 
                return url
            else :
                return '0'
    return 0

###
#  
#   readme: this script is for ais3 2022 , no other use like pwn a government website
#   ~~ THAT'S WHY THIS CODE IS SUPER UGLY ~~
#
###


# main 
## init
if __name__ == '__main__':
    txt_folder_path = 'files/'
    txt_path = []
    result_array = []
    ###### merge_mode 1 = NO merge file  
    ######            0 = output all result to A "output.txt" 
    merge_mode = 0 
## data read


    pathlist = Path(txt_folder_path).glob('**/*.txt')
    for path in pathlist:
        txt_path.append(path)
    for k in range(len(txt_path)) :
        print("########",txt_path[k],"########")
        f = open(txt_path[k])
        data_list = f.readlines()
        dataset = []
        for data in data_list :
            data1 = data.strip('\n')
            data2 = data1.split('\t')
            dataset.append(data2)
    
        dataset = np.array(dataset)
        redata = []
        for i in range(len(dataset)) :
            redata.append(dataset[i][0])
        f.close()
# scan the url
# deny http code : 000 404
        
        for i in range(len(redata)) :
            try:
                tempcode = test(redata[i])
                if tempcode != '0' :
                    result_array.append(tempcode)
            except Exception as e:
                print ('time out detect',end='<===')
                print (redata[i])
        if merge_mode == 0 :
            print(txt_path[k])
            print(txt_folder_path)
            print('output/')
            result_path = str(txt_path[k]).replace(r'files/',r'output/')
            with open(result_path, 'w') as f:
                for i in range(len(result_array)):
                    f.write(result_array[i]+"\n")
            print ("=======>",result_path,"<=====done")
            print ("=======>",result_path,"<=====done")
            print ("=======>",result_path,"<=====done")
            print ("=======>",result_path,"<=====done")
            print ("=======>",result_path,"<=====done")
            result_array = []     



# merge to one file
    if merge_mode == 1 :
        result_path = 'output.txt'
        with open(result_path, 'a') as f:
            for i in range(len(result_array)):
                f.write(result_array[i]+"\n")
        print ("============done=============")