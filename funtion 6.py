#add an if statement and a continue statement to the loop so that it skips when iterator equals"sun".
def sample():
    weather=["snow","rain","sun","summer","winter"]
    for i in weather:
        if i=='sun':
            continue
        print(i)
sample()
