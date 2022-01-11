#square = lambda num: num*num
greaterthan = lambda num: num>3

l = [1,3,4,5,8,9,]
#mymap = list(map(square,l))
#print(mymap)
print(list(filter(greaterthan,l)))

