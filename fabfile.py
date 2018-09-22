# -*- coding: utf-8 -*-

# Usage example:
# fab -H user@host --prompt-for-sudo-password initial-install

from fabric import Connection
from fabric import task


USER = 're9ulus'
ENV_NAME = 'ml'
CONDA_PREFIX = 'source /home/{user}/miniconda3/bin/activate {env_name} && '

# TODO: Add decorator with loggin


@task
def hello(c):
    print('Hello, world!')


@task
def list_files(c):
    c.run('ls -al')

# == Basic install
@task
def update(c):
    c.sudo('apt update', pty=True)

@task
def install_base(c):
    c.sudo('apt-get install tmux vim build-essential unzip git', pty=True)


@task
def install_vim(c):
    c.sudo('apt-get install vim', pty=True)
    c.put('.vimrc', '/home/{}/.vimrc'.format(USER))
    c.run('git clone https://github.com/VundleVim/Vundle.vim.git /home/{}/.vim/bundle/Vundle.vim'.format(USER))
    c.run('vim +PluginInstall +qall')


@task
def initial_install(c):
    update(c)
    install_base(c)
    install_vim(c)
# == End basic install


# == Python, conda, jupyter
@task
def install_miniconda(c):
    print('--- start install miniconda')
    conda_url = 'https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh'
    c.run('wget {}'.format(conda_url), pty=True)
    c.sudo('sh ./Miniconda3-latest-Linux-x86_64.sh', pty=True)
    c.run('rm Miniconda3-latest-Linux-x86_64.sh', pty=True)
    print('--- deon install miniconda')


@task
def create_conda_env(c, env_name=ENV_NAME):
    print('--- start create conda env')
    requirements_file = '/home/{}/requirements.txt'.format(USER)
    c.put('./requirements.txt', remote=requirements_file)
    c.run('/home/{}/miniconda3/bin/conda create --name {} -y'.format(USER, env_name))
    c.run('/home/{}/miniconda3/bin/conda install --channel conda-forge --yes --file {} --name {}'.format(USER, requirements_file, env_name))
    print('--- done create conda env')


@task
def setup_jupyter(c, env_name=ENV_NAME):
    print('--- start setup jupyter')
    jupyter_folder = '/home/{user}/.jupyter/'.format(user=USER)
    prefix = 'source /home/{user}/miniconda3/bin/activate ml && '.format(user=USER)
    c.run(prefix + 'jupyter notebook --generate-config')
    c.run(prefix + 'jupyter notebook password', pty=True)
    
    c.run('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {path}mykey.key -out {path}mycert.pem'.format(
        path=jupyter_folder
    ))
    config = "c.NotebookApp.certfile = u'{path}mycert.pem'\n".format(path=jupyter_folder) + \
             "c.NotebookApp.keyfile = u'{path}mykey.key'\n".format(path=jupyter_folder) + \
             "c.NotebookApp.ip = '*'\n" + \
             "c.NotebookApp.open_browser = False\n" + \
             "c.NotebookApp.port = 9999\n"

    c.run('echo "{config}" >> {path}jupyter_notebook_config.py'.format(config=config, path=jupyter_folder))
    print('--- done setup jupyter')


@task
def setup_python_stack(c):
    install_miniconda(c)
    create_conda_env(c)
    setup_jupyter(c)
# ==


@task
def setup_docker(c):
    print('--- start setup docker')
    c.sudo('apt install apt-transport-https ca-certificates curl software-properties-common', pty=True)
    c.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -', pty=True)
    c.sudo('add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"', pty=True)
    c.sudo('apt update', pty=True)
    c.run('apt-cache policy docker-ce')
    c.sudo('apt install docker-ce', pty=True)
    c.sudo('usermod -aG docker ${USER}', pty=True)
    print('--- done setup docker')


@task
def setup_cuda(c):
    # From https://www.tensorflow.org/install/gpu
    # Add NVIDIA package repository
    c.sudo('apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub')
    c.run('wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb')
    c.sudo('apt install ./cuda-repo-ubuntu1604_9.1.85-1_amd64.deb')
    c.run('wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb')
    c.sudo('apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb')
    c.sudo('apt update')
    # Install CUDA and tools. Include optional NCCL 2.x
    c.sudo('apt install cuda9.0 cuda-cublas-9-0 cuda-cufft-9-0 cuda-curand-9-0 cuda-cusolver-9-0 cuda-cusparse-9-0 libcudnn7=7.2.1.38-1+cuda9.0 libnccl2=2.2.13-1+cuda9.0 cuda-command-line-tools-9-0')
    # Optional: Install the TensorRT runtime (must be after CUDA install)
    c.sudo('apt update')
    c.sudo('apt install libnvinfer4=4.1.2-1+cuda9.0')


# == Other
@task
def install_fasttext(c):
    c.run('wget https://github.com/facebookresearch/fastText/archive/v0.1.0.zip')
    c.run('unzip v0.1.0.zip')
    c.run('cd fastText-0.1.0 && make')
    c.run('rm v0.1.0.zip')


@task
def install_mxnet(c, env_name='ml'):
    """Install CPU version of mxnet to venv `ml`"""
    prefix = 'source /home/{user}/miniconda3/bin/activate {env_name} && '.format(
        user=USER, env_name=env_name)
    c.run('sudo apt-get install graphviz -y', pty=True)
    # TODO: Try mxnet-mkl
    c.run(prefix + 'pip install mxnet')
    c.run(prefix + 'pip install graphviz')


@task
def install_pytorch(c, env_name='ml'):
    """Install PyTorch withoug GPU support"""
    prefix = 'source /home/{user}/miniconda3/bin/activate {env_name} && '.format(
        user=USER, env_name=env_name)
    c.run(
        prefix + '/home/{user}/miniconda3/bin/conda install pytorch-cpu torchvision-cpu -c pytorch'.format(user=USER))


@task
def install_annoy(c, user=USER, env_name=ENV_NAME):
    c.run(CONDA_PREFIX.format(user=user, env_name=env_name) + 'pip install annoy')
# == End Other
