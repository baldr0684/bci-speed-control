from flask import Flask, render_template, make_response
from flask_cors import CORS, cross_origin
import json
import csv
import os
app = Flask(__name__)
CORS(app)
c=0
@app.route('/legoSpeed/')
def getEmotionData():
  try:
     global c
     if c==0:
       dir_path = os.path.dirname(os.path.realpath(__file__))
       print(dir_path)
       executablepath=os.path.join(dir_path,"AverageBandPowers.exe")
       os.startfile(executablepath)
       c=1
     f = open( 'attention.csv', 'r' ) #open the file in read  mode
     for line in f:
       cells = line.split(",")
       data=cells[0]
       print(data)
       data=float(data)
       #print(type(data))
       if data<=1:
         response="1"
         #print("response1")
       elif data>1 and data<=2:
         response="2"
         #print("response2")
       elif data>2:
         response="3"
         #print("response3")
     f.close()
     return response
  except Exception as e:
     print("except")
     return ("0")
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug= True,port=5000) 

