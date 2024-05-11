# Write your code below and press Shift+Enter to execute
def word_count(string, word):
    words = []
    words = string.split()
    Dict = {}
    
    for key in words:
        if (key == word):
            Dict[key] = words.count(key)
            print("Total Count", Dict)

word_count("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go", "Little")             
            
    