def cats():
    catNames=[]
    while True:
        print('Enter the name of cat '+ str(len(catNames)+1)+' (Or enter nothing to stop.):')
        name=input()
        if name=='':
            break
        catNames=catNames+[name]
    print('The cat names are:')
    for name in catNames:
        print(' '+ name)

supplies=['pens','staplers','flame-throwers','binders']
for i in range(len(supplies)):
    print('Index '+ str(i) + ' in supplise is: ' + supplise[i])