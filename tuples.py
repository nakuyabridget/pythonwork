#Use of parentheses is recommended in tupples
#to indicate the start and end of tuple
#Although parentheses are optional
#Explicit is better than implicit

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is ',len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the zoo is ', len(new_zoo))
print('All animals in new zoo are', new_zoo[2])
print('Last animal brought from old zoo is', len(new_zoo)-1+len(new_zoo[2]))