def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/"+data).read().split()
    for i in range(len(f)):
        f[i]=len(f[i])
    return f
print(main("data06.txt"))   
# Read data from file