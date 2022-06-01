import collections
import re
def readFiles():
  pages = {}
  links = {}
  input_file_type=input("smallファイルなら1を、largeファイルなら2を入力してください(半角):")
  file_name="_small"
  if input_file_type=="2":
        file_name=""
        
  print("ファイル読み込み中...")
  with open('data/pages'+file_name+'.txt') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[int(page[0])] = page[1]

  with open('data/links'+file_name+'.txt') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if int(link[0]) in links:
        links[int(link[0])].add(int(link[1]))
      else:
        links[int(link[0])] = {int(link[1])}   
  return pages,links

def dfs(links,pages,start_node_id,target_node_id):
    print("経路を探しています...")
    container=collections.deque();
    # containerにはidとそのnodeに至ったまでの経路を追加
    container.append([start_node_id,pages[start_node_id]])
    checked_node_id=[]#チェック済みのnode
    
    while len(container)>0:
      id,node_path=container.pop()
      if id==target_node_id:
        return True,node_path
      
      #未チェック かつ nodeが次のnodeを持っていたら
      if id not in checked_node_id and id in links:
        #次のnodeを見ていく
        for next_id in links[id]:
          if next_id not in checked_node_id:
            path=node_path+"→"+pages[next_id]#一つ前のnodeのpathに自分を追加する      
            container.append([next_id,path])
            
      checked_node_id.append(id)
      
    return False,node_path

def bfs(links,pages,start_node_id,target_node_id):
      #基本の流れはdfsと同様
    print("経路を探しています...")
    container=collections.deque();
    
    container.append([start_node_id,pages[start_node_id]])
    checked_node_id=[]
    while len(container)>0:
      id,node_path=container.popleft()#キューなのでここだけとり方が違う
      
      if id==target_node_id:
        return True,node_path
      if id not in checked_node_id and id in links:    
        for next_id in links[id]:
          if next_id not in checked_node_id:
            
            path=node_path+"→"+pages[next_id]      
            container.append([next_id,path])
      
      checked_node_id.append(id)
      
    return False,node_path
 
#idを日本語のpathにする関数
def make_path_from_id_array(path_id_array):
      path=""
      for p in path_id_array:
          path+="/"+pages[p] 
      return path

#名前からidを探す関数
def make_id_from_name(name):
    result=-1
    for k, v in pages.items():
      if v==name:
            result=k
    return result      
      

if __name__ == '__main__':
      
  pages,links=readFiles()
  user_select_way=input("dfsで探す場合はdを,bfsで探す場合はbを入力してください(半角):")
       
  start=make_id_from_name(input("スタート地点:")) 
  goal=make_id_from_name(input("ゴール地点:"))
  
  #存在しない地点だった場合-1が返ってくる
  if start!=-1 and goal!=-1:
      if user_select_way=="d":
        result,path=dfs(links,pages,start,goal)
        f = open("data/dfs_way.txt", 'w')  
        f.write(path)
      else:
        result,path=bfs(links,pages,start,goal)
          
      if result:      
        print("経路:"+path)
      else:
        print("経路はありません")  
  elif start==-1:
      print("スタート地点が見つかりません")
  else:
      print("ゴール地点が見つかりません")    
  