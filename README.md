# unit-one-docker
Data engineering zoomcamp course module 1 homework.

## Commands on Windows
Instead of running ```docker run ubuntu``` which may not be what you expect on a Windows machine,
run ```docker run ubuntu bash```and even more ambitious ```docker run -it ubuntu bash```.

Then you should see something like, ```root@dc71d323795f:/#``` which means now you are inside a container.

where the format simply means,
```root```: You are logged in as user.
```dc71d323795f```: The container ID (shortened, they are usually a bit longer)
```:/#```: The root directory inside a Linux system

### Python Version Issue on Windows
Now let's tackle the python version issue.
Since we are running on windows machine ```apt``` doesn't really do much or apply at all. That is because it is a Linux package manager.

So, on Windows, We are running this inside WSL (Ubuntu/Debian) -> bash and the Python version we get is whatever that Linux distro ships as python3

at the moment we want v:3.13 but we have v:3.12, so we need to fix this but how?

1. we can either install python 3.13 from [url]("https://python.org") OR
2. Use ```pyenv``` inside WSL

   ```bash
    sudo apt update
   ```
   ```bash
    sudo apt install -y build-essential libssl-dev zlib1g-dev \
      libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev \
      xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
   ```
  
  Install pyenv
  ```bash
  curl https://pyenv.run | bash
  ```
Add to ~/.bashrc
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Then:
```bash
pyenv install 3.13.0
pyenv global 3.13.0
python --version
```

## Virtual Environments and Data Pipelines

Add thes early on in the gitignore to avoid tracking of these files:

```
*.parquet
*.csv
*.json
data/
```

if files were tracked accidentally.

```bash
git rm --cached '*.file_extension'
```

## Homework SQL Queries Location:

In the README document inside the pipeline directory. Thank you!
