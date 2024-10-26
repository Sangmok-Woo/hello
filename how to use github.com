###깃허브 사용법

working directory(작업 공간) ==>(add) staging area(커밋 전 파일들) 

=> (commit)local repo(커밋 저장소) => (push)remote repo(원격 저장소)

###커밋하는 법

1. git remote add git_test https://github.com/SangMok-Woo/github_test.git
git remote --verbose


2. git add git_test.ipynb
git add .

3. git commit -m "커밋해야지~"

4. git push git_test main


#####클론하는 법

1. git clone https://github.com/TheAlgorithms/Python.git
2.git pull git_test main

