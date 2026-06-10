#Checks unrelated files to make sure model works as expected
def file_check1():
  file_path = Path("/Users/anishbandapelli/Library/Mobile Documents/iCloud~md~obsidian/Documents/Anish's Brain/Computer Science/Data Structures.md")
  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    content = re.sub(r"\-\-\-(.*?)\-\-\-", "", content, flags=re.DOTALL)

  return content

def file_check2():
  file_path = Path("/Users/anishbandapelli/Library/Mobile Documents/iCloud~md~obsidian/Documents/Anish's Brain/Investing/Investing.md")
  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    content = re.sub(r"\-\-\-(.*?)\-\-\-", "", content, flags=re.DOTALL)

  return content

content_check = []

note1 = file_check1()
note2 = file_check2()

content_check.append(note1)
content_check.append(note2)
embeddings = model.encode(content_check)
print(embeddings.shape)
similarities = model.similarity(embeddings, embeddings)
print(similarities)


print(umap_embeddings[:5])