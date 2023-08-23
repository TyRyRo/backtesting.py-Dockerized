# backtesting.py
A Dockerized project that runs a backtesting.py strategy and produces the output of the backtest.

## Project Context
This project contains a Dockerfile that does all the work of downloading, installing and compiling the necessary tools required to run backtesting.py in a Linux environment.

## Dockerfile
### A couple things about the Dockerfile...
1) This container runs ```FROM``` an instance of Pypy3.9
2) We add a user to the container named ```backtester```, whom executes the python code.
3) We copy this project's ```requirements.txt``` file into the container so that the image can do the work automatically of installing the required Python packages.
4) We need to install **TA-Lib** from source code and compile it as an Aarch64 build: ```(--build=aarch64-unknown-linux-gnu)```. Feel free to change this ```--build``` flag's value to whatever you require. **TA-Lib** is a C-based program, so it needs to be installed first before the pip installed ta-lib Python wrapper can be installed.
5) We expose *port 8888* for Jupyter use, but the default ```CMD``` is just running the Strategy.py script via the ```python``` executable.

## How To Use
1) Build the docker image locally: ```docker build . -t <tag>``` (will take some time to download/install all the packages).
2) Run the docker container: ```docker run -p 8888:8888 <tag>```.
3) This will run a container with a ```jupyter notebook``` entrypoint. To access the notebook in your local browser, use the URL/token in the shell output provided by the docker run command.
4) You should now be able to access the project in your local browser via jupyter.
