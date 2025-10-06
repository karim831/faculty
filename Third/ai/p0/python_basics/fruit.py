fruits = {'apple':2.00, 'oranges': 1.50, 'pears': 1.75}; 

def BuyFruit(fruit, numPounds): 
    if fruit not in fruits:
        print('Sorry We Don\'t Have %s' % (fruits)); 
    else:
        cost = fruits[fruit] * numPounds
        print("That'll be %f please" % (cost)) 
        
BuyFruit('apple',2.5);
