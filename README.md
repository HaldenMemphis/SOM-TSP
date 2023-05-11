# SOM-TSP
SOM-TSP is an attempt to solve the traveler problem using the self-organizing map algorithm, and the same was implemented in the project to solve the traveler problem using the dynamic programming algorithm. The performance of using these two methods is compared
## [EN]
This repository implements an attempt to solve the traveler problem with the SOM algorithm
In this SOM algorithm:
+ Use Euclidean distance as the competition mechanism
+ Use normal distribution as a reward for the winner node (winner-take-all)

### DataSet
The dataset in the experiment was selected from a competition called 'Traveling Santa 2018 - Prime Paths' and the competiton was published in the website Kaggle. This is the link of the raw dataset: https://www.kaggle.com/competitions/traveling-santa-2018-prime-paths/data

The raw dataset includes a list of cities and their coordinates, this experiment was conducted with randomly selected data from the raw data.


### How to Run?
All the code files needed to run the project are stored in the `src` directory, the dataset files are placed in the `Data` directory, and the corresponding full run results and partial text files are placed in the `documents` directory.

This project runs in **anaconda** environment. The **anaconda** runtime environment has been exported as the `requirements.yaml` file. Please use this file to create the **anaconda** environment to run the software.

To run this project, run the `main` function inside `src/main.py`. Where the input file is a formatted csv file, and different data can be selected by changing `file_path`. Of course, the learning rate, the maximum number of iterations, and the decrease rate can be modified by passing in the parameters in `som_run`.

## [CN]
本存储库实现了SOM算法解决旅行商问题的尝试
在本SOM算法中：
+ 使用欧几里得距离作为竞争机制
+ 使用正态分布作为对胜利者节点的奖赏（赢家通吃）

### 如何运行？
本储存库的`src`目录下存有运行所需的所有代码文件，数据集文件被放置在`Data`目录下，相应的完整运行结果和部分文本文件被放置在`documents`目录下。

本项目在**anaconda**环境下运行，**anaconda**的运行环境已导出为`requirements.yaml`文件。请使用此文件创建**anaconda**环境以运行软件。

要运行此项目，请运行`src/main.py` 内的`main`函数。其中，输入文件为格式化的csv文件，可通过更改`file_path`来选择不同的数据。当然，学习率，最大迭代次数，和decrease rate可以通过`som_run`内的传入参数进行修改。

###数据集
实验中的数据集是从一个名为 "Traveling Santa 2018 - Prime Paths "的比赛中选出的，该比赛发布在Kaggle网站上。这是原始数据集的链接：https://www.kaggle.com/competitions/traveling-santa-2018-prime-paths/data
原始数据集包括一个城市及其坐标的列表，本实验从原始数据中随机选择数据进行实验。