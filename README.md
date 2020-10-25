# python-code
#Just running some basic functions in python I am a beginner need ideas
list1=["adeen","felix","devansh","satish"]
list2=["priya","aaliya","shreya","neha"]
def fam():
    global list1
    global list2
    print("FAMILY\n","MENS:\t\n",list1,"\nWOMEN:\t\n",list2,"\n")
   #before swapping 
fam()
def swap(a,b):
    global list1
    global list2
    temp=list1[a]
    list1[a]=list2[b]
    list2[b]=temp
def genderchange():
    swap(0,0)
    swap(1,1)
    swap(2,2)
    swap(3,3)
genderchange()
#after swapping
fam()
def couple():
    global list1
    global list2
    print(list1[1],'weds',list2[2])
    print(list1[0],'weds',list2[1])
    print(list1[2],'weds',list2[3])
couple()
print("\n")
genderchange()
couple()
GR="\033[1;31;42m"
print(GR+"THIS IS HOUSEFULL 5😂😂😂")
