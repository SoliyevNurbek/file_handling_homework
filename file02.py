def main(dat:str):
    """
        
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/"+dat).read().split('/n')
    s=0
    for i in f:
        s+=len(i)
    return s

print(main("data02.txt"))

# Read data from file