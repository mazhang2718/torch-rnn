# My process notes for this branch

## Spun up a "deep learning" AMI on Amazon EC2

- Used the "marketplace" and searched for "deep learning"
- Spun it up into a `p2.xlarge` instance, which is about 90 cents an hour
- Tried to do as a spot instance, but couldn't because it was grayed-out. Sent Amazon a ticket asking about this
- ssh'd into the server


## Getting Torch running

- the `th` command didn't work out of the gate ... tho the AMI comes with Torch. 🤔
- went into `~/src/torch` and ran the `install-deps` as described in the Torch docs, but all dependencies were already installed.
- so in the same directory did `./install.sh` ... which clearly installed what I needed, and took advantage of the CUDA and GPUs in the box
- then exited and re-logged in to get everything going
- now the `th` gets me:

```
 ______             __   |  Torch7 
/_  __/__  ________/ /   |  Scientific computing for Lua. 
 / / / _ \/ __/ __/ _ \  |  Type ? for help 
/_/  \___/_/  \__/_//_/  |  https://github.com/torch 
                         |  http://torch.ch 
  
th>
```

Yay!

NOTE: I checked the luarocks packages using `luarocks list` and all of the packages listed in the torch-rnn repo were already installed. Sweet. Same for `python2.7-dev` and `libhdf5-dev`.

The only thing missing was the `torch-hdf5`, which the instructions say we need form GitHub:

```
# We need to install torch-hdf5 from GitHub
git clone https://github.com/deepmind/torch-hdf5
cd torch-hdf5
luarocks make hdf5-0-0.rockspec
```

That worked.

    

## Getting conda environment working

- couldn't use `conda` until added this to `.bashrc`
    `export PATH="/home/ubuntu/src/anaconda2/bin:$PATH"`
- but `conda create --name dogs` ran into permissions problems
- but then couldnt use `sudo conda`. Sigh. 
- So created new env using full path to conda:
    ` sudo /home/ubuntu/src/anaconda2/bin/conda create --name dogs`
- Then: `source activate dogs`


## Prepped the data

- Downloaded a 2013 NYC dog dataset from [this WNYC fusion table](https://fusiontables.google.com/data?docid=1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ#rows:id=1) which has 81,542 rows and 13,803 unique dog names. I didn't do anything to pull out just the unique names.
- used csvkit to grab just the first column of the dog dataset
    `csvcut -c 1 > dog_names.txt`
- 