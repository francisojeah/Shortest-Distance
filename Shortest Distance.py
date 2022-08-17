class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.verticesDict = {}
        self.pathWeight = []

        for x in self.vertices:
            self.verticesDict[x] = []
        

    def addEdge(self, V1, V2):
        for i in self.verticesDict:
            if i == V1:
                if V2 not in self.verticesDict[i]:
                    self.verticesDict[i].append([V2])
                    self.verticesDict[i].sort()
            if i == V2:
                if V1 not in self.verticesDict[i]:
                    self.verticesDict[i].append([V1])
                    self.verticesDict[i].sort()

    def addWeight(self, time):
        for x in self.verticesDict:
            for y in self.verticesDict[x]:
                self.verticesDict[x][self.verticesDict[x].index(y)].append(1)

        if(time in range(1020, 1141)):
            self.verticesDict["lagos"][self.verticesDict["lagos"].index(["ekiti", 1])][1] = 10
            self.verticesDict["ekiti"][self.verticesDict["ekiti"].index(["lagos", 1])][1] = 10

        if(time in range(720, 841)):
            self.verticesDict["ekiti"][self.verticesDict["ekiti"].index(["osun", 1])][1] = 10
            self.verticesDict["osun"][self.verticesDict["osun"].index(["ekiti", 1])][1] = 10
            self.verticesDict["osun"][self.verticesDict["osun"].index(["edo",1])][1] = 10
            self.verticesDict["edo"][self.verticesDict["edo"].index(["osun",1])][1] = 10

        if(time in range(0, 361)):
            del(self.verticesDict["lagos"][self.verticesDict["lagos"].index(["ogun",1])])
            del(self.verticesDict["ogun"][self.verticesDict["ogun"].index(["lagos",1])])

    
    def Path(self, start, end,path = [], totalPath = []):
        path = path +[start]

        if (start == end):
            self.arr = 0
            for i in range(0,len(path)-1):
                self.s = self.verticesDict[path[i]]
                for j in self.s:
                    if(j[0] == path[i+1]):
                        self.arr += j[1]
            totalPath.append(path)
            self.pathWeight.append(self.arr)

        if start not in self.verticesDict:
            return []

        for i in self.verticesDict[start]:
            if i[0] not in path:
                self.Path(i[0],end,path,totalPath)      
       
        return totalPath


Locations = ["edo", "ekiti", "kwara", "lagos", "ogun", "ondo", "osun"]
instance1 = Graph(Locations)

edges = [
    'edo kwara', 
    'edo ondo',
    'edo osun',
    'ekiti ogun',
    'ekiti ondo',
    'ekiti osun',
    'ekiti lagos',
    'kwara lagos',
    'lagos ogun',     
    ]
for edge in edges:
    edge = edge.split(" ")
    instance1.addEdge(edge[0], edge[1])

x = False
while(x is False):
    begin = input("Choose start location: ")
    begin = begin.lower()
    if(begin not in Locations):
        print('Invalid location')
        print(Locations)
    else:
        x = True
x1 = False
while(x1 is False):
    finish = input("Choose destination: ")
    finish = finish.lower()
    if(finish not in Locations):
        print('Invalid location')
        print(Locations)
    else:
        x1 = True

x2 = False
while(x2 is False):
    time = input("Choose time(24H Format) : ")
    if(':'in time):
        times = time.split(':')
    elif('.' in time):
        times = time.split('.')
    else:
        times = [time, 0]
    time1 = int(times[0])*60
    time2 = int(times[1])
    time3 = time1+time2
    if((time1>1380) or (time2>59)):
        print('Invalid time')
    else:
        x2 = True

instance1.addWeight(time3)
PathList = instance1.pathWeight
TP = instance1.Path(begin, finish)
short = min(PathList)
output = ''
for q in TP[PathList.index(short)]:
    output = output + "-"+ q.upper()
print("The shortest Path from ", begin," to ", finish, "is: ", output[1:])



