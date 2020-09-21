#!/usr/bin/python3
import os
import sys
import datetime
import pandas as pd
import subprocess

class learningHelper():

    file_name = str("todolist.txt")
    standardtimeformat = r"%Y-%m-%d %H:%M:%S"

    @classmethod
    def generateTodolist(cls, todostr):
        resstr=''
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(hours=1)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(hours=7)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        #resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(hours=1)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(days=1)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(days=4)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(days=7)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(days=30)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(days=60)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"
        resstr = resstr+'\n'+todostr+"\t\t"+(datetime.datetime.now()+datetime.timedelta(days=90)).strftime(learningHelper.standardtimeformat)+"\t\t"+"notdone"      
        return resstr


    @classmethod
    def sort_todolist(cls):
        #headname=['todo','date','haveDone']
        df = pd.read_csv(cls.file_name,'\t+', engine='python',header=0) 
        ndf = df.sort_values(ascending=True,by=["date"],inplace=False,axis=0)
        
        ndf.to_csv(cls.file_name,sep='\t',index=False) 
    
    #列表中删除
    @classmethod
    def remove_thing(cls,thing):#遍历每一行，有done字符串的，就删除，并且把已完成的放到done.txt中
        pass 


if __name__=="__main__":

    if(len(sys.argv) > 1):
        todothing = sys.argv[1]       
        with open(learningHelper.file_name,'a') as f:
            f.write(learningHelper.generateTodolist(todothing))
            f.close()
            learningHelper.sort_todolist()
    else: 
        learningHelper.sort_todolist()
        #显示当前日期要做的事情


