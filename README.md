# flask-pandas
## on nginx-uwsgi stack

Alpine-based docker image for serving flask via uwsgi and nginx, with support for data analysis and plotting through pandas, seaborn and matplotlib.

Big thanks to [Sebastián Ramírez](https://github.com/tiangolo) who created the [uwsgi-nginx-flask image](https://github.com/tiangolo/uwsgi-nginx-flask-docker) this project is based on. This project avoids sourcing directly `FROM` that image in order to allow building from scratch for different architectures (specifically, ARM).

### Usage
`docker run -v $PWD:/app felixlast/flask-pandas:alpine`, mounting app/ including your [uwsgi.ini](app/uwsgi.ini):

```
app/
  uwsgi.ini
  main.py
```
