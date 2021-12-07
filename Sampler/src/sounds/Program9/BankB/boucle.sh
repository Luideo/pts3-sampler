#!/bin/bash


j=16

for ((i=$j; i<=j+15; i++))
do
    cp pad"$j".wav ./pad"$i".wav
done


	
