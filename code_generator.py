text= 'the old text'
encoded_text='dlo bgh mobh'

def encoded(text):
    
    
    for i in text:
        new_text=text.replace(text,encoded_text)
    return new_text



def decode(text):
    
    
    for i in text:
        new_text=text.replace(encoded_text,text)
    return new_text



print(f'the encoding text is:  {encoded(text)}')  
print(f'the original text is:  {decode(text)}')
