def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=0
    for i in open("data/"+data).read():
        if i.isdigit():
            s+=int(str(i))
    return [s]
print(main("data07.txt"))
    
# Read data from file