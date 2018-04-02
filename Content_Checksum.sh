# cd
# echo Enter a directory
# read DIR
# #cd $DIR
echo press enter to countinue
read DIR
cd /home/solar45/Desktop/test/pics
for i in *; do
  sum=$(base64 $i)
  echo -- "$i"  //  "${sum%% *}.${i##*.}"
done
