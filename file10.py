def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/"+data).read().split('\n')
    maxs=-9632145236521523632
    for i in f:
       if maxs<len(i):
           maxs=len(i)
    return maxs
print(main("data10.txt"))   
# Read data from file