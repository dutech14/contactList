contact_List=[] 
j=int(input("How many contacts do you want to input : "))
i= 0
while(i< j):
    name = input("Enter your name :")
    phone_no = int(input("Enter your phone number : "))
    question=input ("would you like to add more contact : \n Enter YES to Continue \n Enter NO to stop\n")
    if( question == "YES" or question == "yes"):
            i+= 1
    else :
       i = j
    newContact = { 'name':name , 'phone_no' : phone_no }
    contact_List.append(newContact)
    i+= 1

print("this is your contact list")
for i in contact_List:
    print ('Name: ', i['name'])
    print ('Phone_no: ', i['phone_no'])

