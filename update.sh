mkdir -p ./temp
git clone  https://github.com/cdn-x/placeholder.git temp
rm -rf ./temp/.git
rm -rf ./temp/.github
mv ./temp ./placeholder