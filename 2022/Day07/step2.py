def printFolder(folder, compareTo, currentMin):
    if folder.files >= compareTo:
        if folder.files < currentMin:
            currentMin = folder.files
    for child in folder.children:
        currentMin = printFolder(child, compareTo, currentMin)
    return currentMin

def addFilesToParent(folder, total):
    if folder != None:
        folder.files += total
        addFilesToParent(folder.parent, total)

class Folder:
    def __init__(self, name, parent, children, files):
        self.name = name
        self.parent = parent
        self.children = children
        self.files = files

f = open("input.txt", "r")
root = Folder("root", None, [], 0)
currentFolder = root
totalFileSize = 0
for line in f:
    line = line.rstrip()
    if line[0] == "$":
        if line[2:4] == "cd":
            folderName = line[5:]
            if folderName == "/":
                currentFolder = root
                continue
            elif folderName == "..":
                currentFolder = currentFolder.parent
                continue
            else:
                for folder in currentFolder.children:
                    if folder.name == folderName:
                        currentFolder = folder
                continue

    elif line[0:3] == "dir":
        folderName = line[4:]
        newFolder = Folder(folderName, currentFolder, [], 0)
        currentFolder.children.append(newFolder)
        continue
    else:
        fileInfo = line.split(" ")
        currentFolder.files += int(fileInfo[0])
        totalFileSize += int(fileInfo[0])
        addFilesToParent(currentFolder.parent, int(fileInfo[0]))

availableSpace = 70000000 - totalFileSize
print(printFolder(root, 30000000 - availableSpace, 70000000))

f.close()

