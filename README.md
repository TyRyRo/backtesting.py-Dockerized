# backtesting.py
A Dockerized project that runs a backtesting.py strategy and produces the output of the backtest.

## Project Context
This project contains a Dockerfile that does all the work of downloading, installing and compiling the necessary tools required to run backtesting.py in a Linux environment.

## Dockerfile
### A couple things about the Dockerfile...
1) This container runs ```FROM``` an instance of Pypy3.9
2) We add a user to the container named ```backtester```, whom executes the python code.
3) We copy this project's ```requirements.txt``` file into the container so that the image can do the work automatically of installing the required Python packages.
4) We need to install **TA-Lib** from source code and compile it as an Aarch64 build: ```(--build=aarch64-unknown-linux-gnu)```. Feel free to change this ```--build``` flag's value to whatever you require.
5) We expose *port 8888* for jupyter use, but the default ```CMD``` is just running the Strategy.py script via the ```ython``` executable.
