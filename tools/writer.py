

def write_text(name, list):
    """insert file name without format"""
    with open(f"exports/{name}.txt","a") as file:
        for item in list:
            try:
                file.writelines(item+"\n")
            except:
                print(item)
