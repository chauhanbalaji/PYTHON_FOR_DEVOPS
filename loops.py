#list -> data structure which can hold multiple valuse of multiple type 
#Array -> data structure which can hold multiple values of same type
list_of_cloud = ["aws", "Azure", "gcp", "digtal_ocean", "utho"]
cloud = "gcp" #variable

print(list_of_cloud)

#addd a new cloud saleforces

list_of_cloud.append("saleforce")

#add a new cloud IBM
list_of_cloud.append("IBM")

list_of_cloud.insert(2, "Heroku")
print(list_of_cloud)

print(len(list_of_cloud))

#insert "Hello CLOUD" to 0th element of list

list_of_cloud.insert(0,"HELLO cloud")
print(list_of_cloud)

#iteration of list

for cloud in list_of_cloud:
    print("")
    print(cloud)

for i in range(1,11):
    print(i)