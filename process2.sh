#! /bin/bash


echo $1
cd $2
gzip -cd $1 > $1.d
cat $1.d | grep 'utterance\|mappings' > 1.$1
sed -i -e 's/mappings(\[\]).//g' 1.$1
sed '/^\s*$/d' 1.$1 > sprc.$1
rm 1.$1
rm $1.d
mv sprc.$1 $3

