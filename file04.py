def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/"+data).read()
    l=[]
    for u in f:
        if not u.isdigit():
            l.append(u)
    return l

print(main("data04.txt"))
  
# Read data from file