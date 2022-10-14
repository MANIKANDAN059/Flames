def checker(name):
    flames=["f","l","a","m","e","s"]
    j = 6
    count=0
    index=0

    while(len(flames)>1):
        for i in flames:
            count+=1
            if(count==name):
                count=j-(flames.index(i)+1)
                j=j-1
                flames.pop(flames.index(i))
                break;

    flames="".join(flames)

    flame={
        'f':"Friend",
        'l':"Love",
        'a':"Affection",
        'm':"Marriage",
        'e':"Enemy",
        's':"Sister"
    }

    return flame.get(flames)

def flames(name1,name2):

    name1=list(name1.lower())
    name2=list(name2.lower())
    for i in name1:
        for j in name2:
            if(i==j):
                name1[name1.index(i)]=""
                name2[name2.index(j)]=""
                break


    name1="".join(name1)
    name2="".join(name2)
    name=name1+name2
    res = checker(len(name))
    return res

if __name__ == "__main__":
    boy_name = "suriya"
    girl_name = "shyluksha"
    print(flames(boy_name,girl_name))