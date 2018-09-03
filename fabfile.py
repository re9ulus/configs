from fabric import Connection
from fabric import task


IP = '176.9.18.248'
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
    c.run('sudo apt-get install tmux vim build-essential', pty=True)


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
    c.run('/home/re9ulus/miniconda3/bin/conda create --name {} -y'.format(env_name))
    c.run('/home/re9ulus/miniconda3/bin/conda install --channel conda-forge --yes --file {} --name {}'.format(requirements_file, env_name))


@task
def install_vim(c):
    config_repo = 'git@github.com:re9ulus/configs.git'
    c.run('sudo apt-get install vim', pty=True)
    c.run('git clone {}'.format(config_repo))
    c.run('mv ./configs/.vimrc ~/.vimrc')
    c.run('rm -r configs')

# def list_files():
#     connection = Connection(IP, USER)
#     connection.run('ls -a')
