import datetime as date
import json
today = ("{} /{} /{}").format(date.datetime.now().day,date.datetime.now().month,date.datetime.now().year) 

today_waste = {}
today_dic = {}
number_of_bought = int(input("number of stuff u bought today :) "))
for i in range(number_of_bought):

    name_of_product,value = input("name of product and value separated by spaces ").split(" ")

    value = int(value)

    today_waste[name_of_product] = value

    today_dic[today] = today_waste

print(today_dic)
with open ("wastes.json","w") as file:
    json.dump(today_dic,file)

