import matplotlib.pyplot as plt

frequency = {        
 'python':5,
 'big data':10, 
 'crawling':4, 
 'analysis':4, 
 'visualization':4, 
 'machine learning':5, 
'deep learning':6}

lists = sorted(frequency.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.title('Frequency of Word' ) 
plt.bar(x, y)
plt.show()

 
