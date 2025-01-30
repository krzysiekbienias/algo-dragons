import os

domain_dir='/Users/krzysztofbienias/Documents/dev_python/algo-dragons/sandbox/Dane-NF-2405'
file_path=os.path.join(domain_dir,'liczby_przyklad.txt')
with open(file_path, 'r') as file:
    content = file.read()

split_content=content.split('\n')
'Users/krzysztofbienias/Documents/dev_python/algo-dragons/sandbox/Dane-NF-2405'

if __name__=='__main__':
    content