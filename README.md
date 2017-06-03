# Introduction

retrieve_illustration.py can resize, extract tags, vectorize, and display with your images (jpg files or png files) 
by using [illustration2vec](https://github.com/rezoo/illustration2vec)

# Requirements

* anaconda3-4.2.0
* chainer
* illustration2vec

# How to make enviroment
Recommend to make enviroment with [pyenv](https://github.com/pyenv/pyenv)

```
git clone https://github.com/takatsugukosugi/illustration2vec.git
cd illustration2vec
pyenv install anaconda3-4.2.0
pyenv local anaconda3-4.2.0
conda create -n "DL_Frameworks" python=3.5.2 anaconda
pyenv local anaconda3-4.2.0/envs/DL_Frameworks
pip install chainer

```
if you finished making enviroment, type shown blow command

```
python retrieve_illustration.py -h

```

and then return this

```

usage: retrieve_illustration.py [-h] [--version]
                                {resize,vectorize,calculate,search} ...

retrieve_illustration.py -- Search similar illustration using illustration2vec
and cosine similarity

positional arguments:
  {resize,vectorize,calculate,search}
    resize              Resize given image files.
    vectorize           Vectorize given image files.
    calculate           Calculate cosine similarity from given vector.
    search              Search similar images from given image files by using
                        cosine similarity.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
```
# Usage

This script can resize, extract tags, vectorize many image files in directory at a time, 
and can calculate cosine similarity, furthermore can search similar images

1st step (resize : make thumbnail file)

```

python retrieve_illustration.py resize -i [input image file dir/ (should type "/")] -s [size (for example:256)] --outdir [output dir/]

```

2nd step (extract : extracting illustration tags)

```

python retrieve_illustration.py vectorize -i [input resized image file dir/ (should type "/")] -t [threshold (for example:0.1)] -v False --outdir [output dir/]

```

3rd step (extract : vectorize illustration tags)

```

python retrieve_illustration.py vectorize -i [input resized image file dir/ (should type "/")] -t [threshold (for example:0.1)] -v True --outdir [output dir/]

```

4th step (calculate : calculate cosine similarity by using vectorized tags)

```

python retrieve_illustration.py calculate -i [input csv file (can get 3th step)] -t [categories name] --outdir [output dir/]

```

5th step (search : make jpg file to display Top 10 similar illustrations)

```

python retrieve_illustration.py search -i [input csv file (can get 4th step)] -t [categories name] --outdir [output dir/]

```

