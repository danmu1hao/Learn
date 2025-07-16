import os
print(os.path.dirname(__file__))

def read_data() -> str:
    with open(os.path.dirname(__file__)+"/data.md","r",encoding="utf-8") as f:
        return f.read()

def get_chunks() -> list[str]:
    content: str=read_data()
    chunk: list[str] = content.split('\n\n')
    return chunk

if(__name__=='__main__'):
    chunks: list[str] = get_chunks()
    for c in chunks:
        print(c)
        print("-------------------------")