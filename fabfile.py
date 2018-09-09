from fabric import Connection
from fabric import task


IP = ''
USER = 're9ulus'


@task
def hello(c):
    print('Hello, world!')


@task
def list_files(c):
    c.run('ls -al')

@task
def update(c):
    c.run('sudo apt update', pty=True)

@task
def install_base(c):
    c.run('sudo apt-get install tmux vim build-essential unzip', pty=True)


@task
def install_miniconda(c):
    conda_url = 'https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh'
    c.run('wget {}'.format(conda_url), pty=True)
    c.run('sudo sh ./Miniconda3-latest-Linux-x86_64.sh', pty=True)
    c.run('rm Miniconda3-latest-Linux-x86_64.sh', pty=True)
    # TODO: Add to .bashrc
    # export PATH=~/miniconda3/bin:$PATH


@task
def create_conda_env(c):
    env_name = 'ml'
    requirements_file = '/home/{}/requirements.txt'.format(USER)
    c.put('./requirements.txt', remote=requirements_file)
    c.run('/home/{user}/miniconda3/bin/conda create --name {} -y'.format(USER, env_name))
    c.run('/home/{user}/miniconda3/bin/conda install --channel conda-forge --yes --file {} --name {}'.format(USER, requirements_file, env_name))


@task
def install_vim(c):
    c.run('sudo apt-get install vim', pty=True)
    c.put('.vimrc', '/home/{}/.vimrc'.format(USER))
    c.run('git clone https://github.com/VundleVim/Vundle.vim.git /home/{}/.vim/bundle/Vundle.vim'.format(USER))
    c.run('vim +PluginInstall +qall')


@task
def setup_jupyter(c):
    env_name = 'ml'
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


@task
def setup_docker(c):
    c.run('sudo apt install apt-transport-https ca-certificates curl software-properties-common', pty=True)
    c.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -', pty=True)
    c.run('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"', pty=True)
    c.run('sudo apt update', pty=True)
    c.run('apt-cache policy docker-ce')
    c.run('sudo apt install docker-ce', pty=True)
    c.run('sudo usermod -aG docker ${USER}', pty=True)


@task
def install_fasttext(c):
    c.run('wget https://github.com/facebookresearch/fastText/archive/v0.1.0.zip')
    c.run('unzip v0.1.0.zip')
    c.run('cd fastText-0.1.0 && make')
    c.run('rm v0.1.0.zip')


@task
def install_mxnet(c, env_name='ml'):
    """Install CPU version of mxnet to venv `ml`"""
    prefix = 'source /home/{user}/miniconda3/bin/activate {env_name} && '.format(user=USER, env_name=env_name)
    c.run('sudo apt-get install graphviz -y', pty=True)
    # TODO: Try mxnet-mkl
    c.run(prefix + 'pip install mxnet')
    c.run(prefix + 'pip install graphviz')


@task
def install_pytorch(c, env_name='ml'):
    """Install PyTorch withoug GPU support"""
    prefix = 'source /home/{user}/miniconda3/bin/activate {env_name} && '.format(
        user=USER, env_name=env_name)
    c.run(prefix + '/home/{user}/miniconda3/bin/conda install pytorch-cpu torchvision-cpu -c pytorch'.format(user=USER))
