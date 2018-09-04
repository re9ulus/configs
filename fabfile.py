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
