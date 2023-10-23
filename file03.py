def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/"+data).read()
    l=[]
    for u in f:
        if u.isdigit():
            l.append(u)
    return l

print(main("data03.txt"))

# Read data from file
