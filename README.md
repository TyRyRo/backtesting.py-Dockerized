# backtesting.py
A Dockerized project that runs a backtesting.py strategy in a Jupyter notebook with optional graphical plotting (see "Graphical Plotting" below).

## Project Context
This project contains a Dockerfile that does all the work of downloading, installing and compiling the necessary tools required to run the backtesting.py library in a Linux environment.

## Dockerfile
### A couple things about the Dockerfile...
1) This container runs ```FROM``` an instance of Pypy3.9
2) We add a user to the container named ```backtester```, whom executes the python code.
3) We copy this project's ```requirements.txt``` file into the container so that the image can do the work automatically of installing the required Python packages.
4) We need to install **TA-Lib** from source code and compile it as an Aarch64 build: ```(--build=aarch64-unknown-linux-gnu)```. Feel free to change this ```--build``` flag's value to whatever you require. **TA-Lib** is a C-based program, so it needs to be installed first before the pip installed ta-lib Python wrapper can be installed.
5) We expose *port 8888* for Jupyter use.
# Important
6) This project utilizes a self-signed certificate + key pair to run Jupyter Notebook in your local browser via TLS. The certificate and key are in the local /ssl directory. The Jupyter ```ENTRYPOINT``` command in the Dockerfile uses them to run over https. When you run this in your browser, you may skip the warning as long as you understand that it is being caused by a self-signed certificate. As long as you are running this on an internal trusted network (aka 127.0.0.1 aka localhost) and not reaching out to the internet, you should not be at risk of someone impersonating a remote website that has the provided private key, allowing them to decrypt your Jupyter traffic.

## Use Your Own Strategy
1) All you have to do is add your own backtesting.py strategy file to the top level of this project as a .ipynb file called ```Strategy.ipynb```.

## How To Use
1) Build the docker image locally: ```docker build . -t <tag>``` (will take some time to download/install all the packages).
2) Run the docker container: ```docker run -p 8888:8888 <tag>```.
3) This will run a container with a ```jupyter notebook``` entrypoint. To access the notebook in your local browser, use the URL/token in the shell output provided by the docker run command.
4) You should now be able to access the ```Strategy.ipynb``` backtesting.py strategy and run it in your local browser via jupyter.

## Graphical Plotting
1) Use the built in backtesting.py ```backtesting.plot()``` function in your strategy code to plot a visual representation in your jupyter notebook.
