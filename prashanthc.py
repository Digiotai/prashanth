#

import redis
#creating connection with localhost to redis database
r = redis.Redis(host='localhost', port=6379, db=0)
R=redis.StrictRedis(host='localhost',port=6379, db=0)

#check if database list is created then pull out data else create empty list
if R.exists("mylist")==1:
    list =(r.lrange('mylist',0,-1))
    list_task=[i.decode("utf-8") for i in list]
else:
    list_task=[]

#add task until user provide blank task             
condition=True
while condition:
    task=input('Enter a chore or task  ')
    if len(task)==0:
        condition=False

        #display all task
        for i in list_task:
                print(i)
        remove=input('will you like to remove any task (yes/no) ')

        #remove task given by user
        if remove=='yes':
              task_to_remove=str(input('The task you want to remove  '))
              list_task.remove(task_to_remove)
              for i in list_task:
                print(i)
              r.lrem("mylist",0,task_to_remove)

    else:
        list_task.append(task)
        r.rpush('mylist',task)
        
#print all task
print(list_task)
        
      
