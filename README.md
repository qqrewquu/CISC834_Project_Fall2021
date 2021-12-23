## A Comparison Study of Two Inference of Environment Dependencies for Python Code Snippets Tools

This repository is the implementation of [A Comparison Study of Two Inference of Environment Dependencies for Python Code Snippets Tools](https://www.overleaf.com/5697861924shhgwyytbhkd).



## Dataset

The dataset including 2500 python gists under `datasets/` folder



## Usage

>**For evaluting Gistable on datasets please run following:** 

`cd RQ1_gistable/index.js`

uncommented `const SOURCE_PATH = path.resolve(__dirname, '../datasets/gistable-evaluated-gists')`


run `RQ1_gistable/code/RQ1_Gistable.ipynb`

>**For evaluting DockerizeMe on datasets please run following:** 

`cd RQ1_gistable/index.js`

uncommented `const SOURCE_PATH = path.resolve(__dirname, '../datasets/dockerizeme-evaluated-gists')`

run `RQ2_dockerizeme/code/RQ2_Dockerizeme.ipynb`

>**For recording the categories of exit status of fixed gists from Gistable and DockerizeMe**


run `RQ3_error_analysis/RQ3.ipynb`


## Results

The results from three research questions have been saved at `results/` folder