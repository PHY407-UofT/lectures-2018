# lectures

This repository contains the material for the PHY407 lectures. I will update it as the class goes. How to retrieve the lectures will not be too much different from "hitting" "sync" one in a while, except for the very first time you "initiate" "downloading" the material.

I am using all these annoying double quotes because I will be using git, and these words are not part of the git vocabulary. You will not "sync" or "downwload" the material, you will pull it from the repository. And you will not "initiate downloading the material", you will clone this repo(sitory). And with the procedure I am about to describe, you will not "hit" any button, you will type command lines in a remote terminal (no need to install anything).

The procedure I am about to describe will work for anyone in the class, on any OS (Windows, OSX, Unix, Android, iOS) or platform (laptops, tablets, even smartphones for the most masochistically-inclined of you). The reason is simple: all you need is a browser and an internet connection. It is a minimally working example. You could also do everything on your computer and use a git client with a graphical user interface (google 'best git client for [insert your OS here]'), but if you know how to work your way around it, my guess is that you don't need these instructions.

## Initial steps

At the very beginning of this class, you will need to clone this repository. Once you have cloned it, you will be able to easily update the contents as the course progresses.

1. First of all, go there and log in with your utorid:
https://utoronto.syzygy.ca
You will want to bookmark this link. Syzygy is a fantastic new service run by the Pacific Institute of Marthematical Sciences in Vancouver, and is hosted on Compute Canada's servers. Once you've logged in, start the server.

2. Start a terminal. In the top right corner, below the "Logout" and "Control panel" buttons, hit "New". In the drop-down menu that appears, hit "Terminal".

3. Go to wherever you want the future folder to be located. It could be your home folder:

```cd ~```

or it could be a PHY407 folder that you created:

```cd ~```
```mkdir PHY407```
```cd PHY407```

4. Clone the repository. If you do not have a GitHub account at this point, create one. You may also want to apply for a Student Developer Pack (https://education.github.com/pack), which gives you access to a lot of features that are not free otherwise.

Somewhere on the top right web page of this repository, there is a green "Clone or download" button. Click on it, a URL shows up. Copy it, and in the terminal, type ```git clone``` and paste the url. It should look like
```git clone https://github.com/some-path/lectures```
Hit return. You have cloned the repository.

## Subsequent steps.

1. I will update this repo frequently. Every time you want to access the freshest version of the material, go to a terminal (repeat step 2 above if needed), go to the folder where the repo is (```cd ~/bla-bla/lectures```) and type:

```git pull```

and that's it!

2. Opening the material files: go to your syzygy home page, navigate to the folder where the repo is located. The lecture material is mostly in the form of ```.ipynb``` files. You can open then and read them from syzygy directly. All the code will run on the Compute Canada servers, remotely.

**Procedure to fix edits?**
