def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=5426525412541252422512
    for i in open("data/"+data).read():
        if i.isdigit():
            if int(str(i))<s:
                s=int(str(i))
    return s
print(main("data09.txt"))
# Read data from file