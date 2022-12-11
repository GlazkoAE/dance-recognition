# ITMO action recognition task: dance recognition

## Dataset
Original dataset Kinetics 700-2020 ([paper](https://arxiv.org/abs/2010.10864))
contains labels, YouTube ids and timecodes. It`s available for downloading 
[here](https://storage.googleapis.com/deepmind-media/Datasets/kinetics700_2020.tar.gz).

Dancing dataset contains only dance types. 
It was created with [download_data.py](data%2Fdownload_data.py) and [videos_to_frames.py](data%2Fvideos_to_frames.py).

#### Usage
Download original dataset, unzip .csv files to [data](data) directory and run:

Windows
```angular2html
pip install -r requirements.txt
python ./data/download_data.py dancing
python ./data/videos_to_frames.py
```

Linux / Mac
```angular2html
pip install -r requirements.txt
python3 ./data/download_data.py dancing
python3 ./data/videos_to_frames.py
```
