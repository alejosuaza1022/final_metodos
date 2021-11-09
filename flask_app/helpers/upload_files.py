import os
import uuid
from matplotlib.pyplot import figure, ioff, setp, plot, title, xlabel, ylabel, scatter
import numpy as np


def name_temp_file(file_name, ext):
    random_file_name = ''.join(
        [file_name, str(uuid.uuid4().hex), str(uuid.uuid1().hex)])
    random_file_name = ''.join([random_file_name, ext])
    path = ''.join([os.getenv('TMPDIRS3'), random_file_name])
    return random_file_name, path


# ---------------------
def _graph_rk(filename, xs, ys, tit, labelx, labely):
    fig = figure(figsize=(8, 8), frameon=True)  # Se ag
    plot(xs, ys)
    title(tit)
    xlabel(labelx)
    ylabel(labely)
    plot()
    fig.savefig(filename, bbox_inches="tight", pad_inches=0.1)


def upload_file(file_name, client, obj_name):
    client.upload_file(file_name, os.getenv('BUCKET'), obj_name, ExtraArgs={
        'ACL': 'public-read'})


def remove_tmp_file(filename):
    os.remove(filename)


def generate_link(filename):
    return ''.join([f"https://{os.getenv('BUCKET')}.s3.amazonaws.com/", filename])


def graph_rk(s3_client, filename, xs, ys,  fun, aux=0):
    file, path = name_temp_file(filename, '.jpeg')
    title = f"Runge Kutta orden superior\n{fun}"
    xlabel = 'X'
    ylabel = 'Y'
    if aux == 1:
        title = f"Runge Kutta 4to orden \n{fun}"
    _graph_rk(path, xs, ys, title, xlabel, ylabel)
    upload_file(path,
                s3_client, file)
    remove_tmp_file(path)
    return generate_link(file)


def _graph_lr(filename, x, y, yest, R):
    fig = figure(figsize=(8, 8), frameon=True)  # Se ag
    scatter(x, y)
    plot(x, yest)
    tit = f"Linear Regression"
    title(str((f"{tit}, R ", " : ", R, )))
    plot()
    fig.savefig(filename, bbox_inches="tight", pad_inches=0.1)


def graph_lr(s3_client, filename, x, y, yest, R):
    file, path = name_temp_file(filename, '.jpeg')
    _graph_lr(path, x, y, yest, R)
    upload_file(path,
                s3_client, file)
    remove_tmp_file(path)
    return generate_link(file)


