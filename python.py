#Loops
1.For loop

(i)list_of_names = ['A', 'B', 'C']
for name in list_of_names:
    print(name)

(ii)for i in range(10):
    print(i)


(iii)for i in range(len(list_of_names)):
    print(f"Item in index = {i} is {list_of_names[i]}") #0

(iv)start = len(list_of_names) - 1
end = -1
for i in range(start,end, -1):
    print(f"Item in index = {i} is {list_of_names[i]}") #0


2.While loop

(i) while a<10:


(ii)while True:
  break 

(iii)  continue : Ends a iteration of a Loop 
 break : Ends the Loop

#Lists

(i)list.count(x)- counts the number of times an element appears in the list 

(ii)list.append(x)-adds a single element to the list at a time

(iii)list.extend(x+y)-adds multiple elements to a list at a time

(iv)list.sort()-sorts list in ascending order. For descing order use as list.sort(reverse=True)

(v)list[0]- finds the 0th(1st) index in a list


#Dictionary
(i)d["hey"chat]=1 - This is how to add a key value pair to a dictionary

(iimy_dict.update({'grape': 7})- This is how to add a key value pair to a dictionary

(iii)my_dict = {**my_dict, 'mango': 4}-  This is how to add a key value pair to a dictionary

(iv) for key,value in dict.items():- Iterate through key and value in a dictionary
    dict[key.upper()]=value

(v)dict.get("banana")- finds value associated with key

(vi)max/min(dict,key=dict.get)- finds max or min value and returns the key


#Strings

1.string.split(" ")-Splits the string into different elements in form of a list



                                                                                  

