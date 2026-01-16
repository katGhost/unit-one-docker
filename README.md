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

## Virtual Environments and Data Pipelines

