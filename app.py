from flask import Flask,request,render_template,jsonify
import json



obj=Flask(__name__)


@obj.route('/')


@obj.route('/cal',methods=["GET"])
def math_operation():
    oper=request.json["oper"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    
    if oper=="add":
        result=int(num1)+int(num2)
    elif oper=="multi":
        result=int(num1)*int(num2)
    elif oper=="div":
        result=int(num1)//int(num2)
    else:
        result=int(num1)-int(num2)

    return "the operation is {} the result is {}".format(oper,result)


def welcome():
    return "Welcome to Flask Day1"


if __name__=='__main__':  #if you want to run in standalone mode
    obj.run()

