# SOM-TSP
SOM-TSP is an attempt to solve the traveler problem using the self-organizing map algorithm, and the same was implemented in the project to solve the traveler problem using the dynamic programming algorithm. The performance of using these two methods is compared
### [EN]
This repository implements an attempt to solve the traveler problem with the SOM algorithm
In this SOM algorithm:
+ Use Euclidean distance as the competition mechanism
+ Use normal distribution as a reward for the winner node (winner-take-all)

### [CN]
本存储库实现了SOM算法解决旅行商问题的尝试
在本SOM算法中：
+ 使用欧几里得距离作为竞争机制
+ 使用正态分布作为对胜利者节点的奖赏（赢家通吃）

## DataSet
The dataset in the experiment was selected from a competition called 'Traveling Santa 2018 - Prime Paths' and the competiton was published in the website Kaggle. This is the link of the raw dataset: https://www.kaggle.com/competitions/traveling-santa-2018-prime-paths/data

The raw dataset includes a list of cities and their coordinates, this experiment was conducted with about 8000 randomly selected data from the raw data.
