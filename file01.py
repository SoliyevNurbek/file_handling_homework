def main(dat:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/"+dat).read()
    l=[]
    for i in f:
        if not i==',':
            l.append(int(str(i)))
    return l

print(main("data01.txt"))

# Read data from file