#!/bin/bash

sudo apt install gcc
sudo apt install g++
sudo apt install fpc
sudo apt install python3
sudo apt install curl
curl —proto '=https' —tlsv1.2 -sSf https://sh.rustup.rs | sh 
source $HOME/.cargo/env
source ~/.profile 
git clone https://github.com/pbalykov/nejudge.git
mkdir nejudge/pos
mkdir nejudge/rez
mkdir nejudge/pos/Demo\ contest
mkdir nejudge/pos/Demo\ contest/1 nejudge/pos/Demo\ contest/2
mkdir nejudge/rez/Demo\ contest
mkdir nejudge/rez/Demo\ contect/1
mkdir nejudge/rez/Demo\ contect/2


