def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/"+data).read()
    l=0
    m=0
    for u in f:
        if u.isdigit():
            l+=1
        else :
            m+=1
    return [l,m]

print(main("data05.txt"))
# Read data from file