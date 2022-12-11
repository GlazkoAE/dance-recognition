# ITMO action recognition task: dance recognition

## Dataset
Original dataset Kinetics 700-2020 ([paper](https://arxiv.org/abs/2010.10864))
contains labels, YouTube ids and timecodes. It`s available for downloading 
[here](https://storage.googleapis.com/deepmind-media/Datasets/kinetics700_2020.tar.gz).

Dancing dataset was created with [download_data.py](data%2Fdownload_data.py) and contains only dace types.

#### Usage
Download original dataset, unzip .csv files to [data](data) directory and run `python ./data/download_data.py dancing`
