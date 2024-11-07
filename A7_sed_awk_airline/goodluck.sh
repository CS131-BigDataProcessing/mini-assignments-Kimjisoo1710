#Append the text '-  This is a hit!' at the end of every line
sed 's/$/ -  This is a hit!/' goodluck.txt

#Number each line in the lyrics (Hint* use N and keep in mind line break (\n))
sed = goodluck.txt 
#N: Appends the next line (which is the actual content) to the current pattern space.
#s/\n/ /: Substitutes the newline character between the line number and the actual line with a space, so that the number and text are displayed on the same line.
sed = goodluck.txt | sed 'N;s/\n/ /' 

#Print only lines 22-27 (p stands for print)
sed -n '22,27p' goodluck.txt

#Replace multiple words in the song (all instances of each word)
   # replace babe with girl
   # replace good with bad
   # replace love with tacos
sed -e 's/babe/girl/g' -e 's/good/bad/g' -e 's/love/tacos/g' goodluck.txt
#If want to save changes back to the file, use -i
sed -i -e 's/babe/girl/g' -e 's/good/bad/g' -e 's/love/tacos/g' goodluck.txt
#if case-insensitive
sed -e 's/babe/girl/gi' -e 's/good/bad/gi' -e 's/love/tacos/gi' goodluck.txt
#gi: The g flag replaces all occurrences in a line, and the i flag makes the search case-insensitive.



