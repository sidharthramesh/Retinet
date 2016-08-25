import os

def paths_to_csv(path='test/'):
    for i,j,k in os.walk('test/'):
        paths=k
    image=['image,level']
    new_paths=[]
    for path in paths:
        path+=',0'
        new_paths.append(path)
    new_paths.sort()
    new_paths=image+new_paths
    with open('data/new_trainLabels.csv','wb') as f:
        f.write(os.linesep.join(new_paths))


if __name__=='__main__':
    paths_to_csv()
