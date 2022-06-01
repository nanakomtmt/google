# Google STEP Class 4 Homework

## 準備

```
以下のようなディレクトリ構成にしてください
step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   ├── pages.txt
│   └── dfs_way.txt
├── .gitignore
├── README.md
├── main.py

```

### 実行方法

テスト環境: Python 3.9.2

```shell
python3 main.py
```

1. small ファイルなら 1 を、large ファイルなら 2 を入力してどちらかを選んでください
   　　（！今 dfs を large ファイルの方で実行しようとするとメモリ不足？でうまくいきません、、）

2. dfs か bfs かを選んでください

3. スタート地点、ゴール地点を入力してください

4. 経路が出力されます　 dfs だと長過ぎて見れなかったことがあったのでファイル(dfs_way.txt)を用意します

### 結果

・dfs と bfs を比べると、bfs のほうが最短経路を導けるし見つかるのも速いなと思いました。
・large × dfs 以外はうまくいきました。
　 dfs を大きなファイルでやったときに、一度は実行に 1 時間ほどかかったうえに後ろの方をチェックしたところ繋がりがみられなかったので調査中です。
　もし間違ってるところ見つけたら教えてほしいです。
