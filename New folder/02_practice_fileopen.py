
def readfiel(filename):
    try:
        with open(filename,'r') as f: 
            print(f.read())
    except Exception as e:
        print(f"there is no files availbale {e}") 
'''try:
    f = open("file.txt",'r')
    f.close()
except:
    print(f"there is no file ") '''
readfiel("1.txt")