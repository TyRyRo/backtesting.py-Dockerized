FROM pypy:3.9

RUN useradd -ms /bin/bash backtester

WORKDIR /home/backtester

COPY requirements.txt ./

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
  && tar -xzf ta-lib-0.4.0-src.tar.gz \
  && rm ta-lib-0.4.0-src.tar.gz \
  && cd ta-lib/ \
  && ./configure --prefix=/usr --build=aarch64-unknown-linux-gnu \
  && make \
  && make install \
  && cd ~ \
  && rm -rf ta-lib/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R backtester Strategy.ipynb
RUN chown -R backtester requirements.txt

EXPOSE 8888/tcp

USER backtester

ENTRYPOINT [ "jupyter", "notebook", "--no-browser", "--ip=0.0.0.0" ]
