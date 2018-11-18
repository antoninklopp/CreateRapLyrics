# Original project

This project is a fork from https://github.com/robbiebarrat/rapping-neural-network  

I created it to be able to generate a song directly from a name of an artist. 

# How to use it

First, go to the genius website to create an API key, that will be used to download the songs, used 
to train the model.  
Than export this key under the name : GENIUS_TOKEN on your system

```console
me@machine:~$ export GENIUS_TOKEN="api_token_from_genius_website"
```

Install the requirements from the requirements.txt file using  

```console
me@machine:~$ pip3 install -r requirements.txt
```

You can now launch the main.py

```console
me@machine:~$ python3 main.py artist_name
```