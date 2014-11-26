# Nano-chan

![Nano Shinonome](http://38.media.tumblr.com/f211e5ead70776356ae6a3bedb2544e0/tumblr_mobiyrko391qd7h1xo2_500.gif)

Nano-chan is a IRC bot for #nethaus on irc.freenode.net

She is based off of the character [Nano Shinonome] from the anime [Nichijou].

From [Nichijou Wikia]:

>Nano Shinonome is a robot created by Professor Shinonome (Or simply, Hakase). Nano lives with Hakase and manages the household. She is constantly being upgraded by Hakase without prior knowledge or approval. This leads to strange situations that Nano worries might reveal her android identity to others.

# Features

The feature set is based on Nano's abilities on the show. 

From [Nichijou Wikia]:

>Hakase gave Nano many hidden abbilities, but Nano herself usually learns about them the first time she uses them. One of Nano's special abilities is to dispense pastries. Nano's limbs also come off at random, at her great surprise every single time that she comes apart. Nano is usually unappreciative of and embarrassed by her mostly useless gifts.

These include:

- A rollcake dispenser in her left arm (after some time, it became a fish cake dispenser).

- A sweet bun dispenser in her forehead.

- Her toes comes off easily, and has a USB flash drive concealed inside (its storage is 1GB). Her big toe in particular can be launched like a rocket when the key on her back is turned manually (This is actually the key's only purpose).

- She has a digital watch built into her right arm.

- Has an in-built cuckoo clock. When the clock rings, the cuckoo clock springs out of her forehead.

- She has a gun installed in her hand, which fires soybeans instead of bullets.

- Her right hand is rocket-propelled, but it usually flies off at random. It can fly for a very long time, and can travel very long distances: this was best shown when the fist was accidentally launched and flew around the town for a rather long time, only stopping after it hit Misato Tachibana on the head.

# Installation

- Create and activate your virtualenv

```sh
virtualenv venv
source venv/bin/activate
```

- Install our requirements via pip

```sh
pip install -r requirements.txt
```

- Make a copy of the settings.ini.EXAMPLE file and fill it in with your host, port, nick, real name info and channel to join.

```sh
cp settings.ini.EXAMPLE settings.ini
```

# Running tests

To run all tests, cd into the nanochan folder and run this command:

```sh
trial tests
```

# Running 

After setting up your settings.ini file, run the following commands in the nanochan directory.

```
twistd -n shinolabs
```
 
**Nano-chan was started by painstakingly hand-copying the lovely bot/networking tutorial created by [New Coder]. The tutorial can be found [here].**

[Nano Shinonome]:http://nichijou.wikia.com/wiki/Nano_Shinonome
[Nichijou]:https://www.youtube.com/watch?v=HQ7bC9XycU0
[Nichijou Wikia]:http://nichijou.wikia.com/wiki/Nano_Shinonome
[New Coder]:http://newcoder.io/
[here]:http://newcoder.io/~drafts/networks/
