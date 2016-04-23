import sys
import re
import string

filename=sys.argv[-1]
file_pointer=open(filename,'r')
file_in_memory=file_pointer.read()
file_in_memory=file_in_memory.replace("'s", '').split()
file_in_memory=' '.join(file_in_memory)
file_in_memory=file_in_memory.replace("'ll", '').split()
file_in_memory=' '.join(file_in_memory)
file_in_memory=file_in_memory.replace("'ve", '').split()
file_in_memory=' '.join(file_in_memory)
file_in_memory=file_in_memory.replace("'d", '').split()
file_in_memory=' '.join(file_in_memory)
file_in_memory=file_in_memory.replace("'t", '').split()
file_in_memory=' '.join(file_in_memory)
raw= file_in_memory.translate(string.maketrans("",""), string.punctuation)
file_pointer.close()
write_file_pointer=open(filename,'w')
write_file_pointer.write(raw)
write_file_pointer.close()

