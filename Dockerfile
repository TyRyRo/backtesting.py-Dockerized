FROM pypy:3.9

RUN useradd -ms /bin/bash backtester

WORKDIR /home/backtester

COPY requirements.txt .

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
  && tar -xzf ta-lib-0.4.0-src.tar.gz \
  && rm ta-lib-0.4.0-src.tar.gz \
  && cd ta-lib/ \
  && ./configure --prefix=/usr --build=aarch64-unknown-linux-gnu \
  && make \
  && make install \
  && cd /home/backtester \
  && rm -rf ta-lib/

RUN pip install --no-cache-dir -r requirements.txt \
  && rm requirements.txt

COPY ./ssl /etc/ssl
COPY Strategy.ipynb .

RUN chown -R backtester Strategy.ipynb
RUN chown -R backtester /etc/ssl/key.pem /etc/ssl/cert.pem

EXPOSE 8888/tcp

USER backtester

ENTRYPOINT [ "jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--certfile=/etc/ssl/cert.pem", "--keyfile=/etc/ssl/key.pem" ]
