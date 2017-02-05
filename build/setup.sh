#!/bin/bash
 
echo "Do you want to download Anaconda?(y/n) "
read -r input
if [ "$input" = 'y' ] || [ "$input" = 'Y' ]
then
    echo "Downloading anaconda"
    wget "https://repo.continuum.io/archive/Anaconda2-4.3.0-Linux-x86_64.sh" -o anaconda.sh
    bash anaconda.sh
fi
echo "Enter the path where anaconda is installed:"
read -r anacondaPath
if [ ! -z "$anacondaPath" ]
then
     ls "$anacondaPath/bin/python" 2&>1 /dev/null
     ret=$?
     if [ $ret -eq 0 ]
     then
         echo "$anacondaPath/bin/python"
         echo "Downloading NLTK libraries"
         $anacondaPath/bin/python ./downloadNLTK.py
         ret=$?
         if [ $ret -ne 0 ]
         then
             echo "Error in downloading NLKT libraries"
             echo "Try again and run the text analytics file"
         fi
         $anacondaPath/bin/conda install textblob
     else
        echo "Invalid Path specified"
     fi
fi
