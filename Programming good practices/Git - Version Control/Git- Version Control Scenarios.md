# Git version control scenarios. 

## Scenario #1

Let's walk through the Git commands that go along with each step in the scenario you just observed in the video.

### Step 1: You have a local version of this repository on your laptop, and to get the latest stable version, you pull from the develop branch.



1. Switch to the develop branch
```git
git checkout develop
```

2. Pull the latest changes in the develop branch
```git
git pull
```


### Step 2: When you start working on this demographic feature, you create a new branch called demographic, and start working on your code in this branch.

3. Create and switch to a new branch called demographic from the develop branch
```git
git checkout -b demographic
```
4. Work on this new feature and commit as you go
```git
git commit -m 'added gender recommendations'
git commit -m 'added location specific recommendations'
```

### Step 3: However, in the middle of your work, you need to work on another feature. So you commit your changes on this demographic branch, and switch back to the develop branch.
5. Commit your changes before switching
```git
git commit -m 'refactored demographic gender and location recommendations '
```
6. Switch to the develop branch
```git
git checkout develop
```

### Step 4: From this stable develop branch, you create another branch for a new feature called friend_groups.
7. Create and switch to a new branch called friend_groups from the develop branch
```git
git checkout -b friend_groups
```

### Step 5: After you finish your work on the friend_groups branch, you commit your changes, switch back to the development branch, merge it back to the develop branch, and push this to the remote repository’s develop branch.
8. Commit your changes before switching
```git
git commit -m 'finalized friend_groups recommendations '
```

9. Switch to the develop branch
```git
git checkout develop
```

10. Merge the friend_groups branch into the develop branch
```git
git merge --no-ff friends_groups
```

11. Push to the remote repository
```git
git push origin develop
```

### Step 6: Now, you can switch back to the demographic branch to continue your progress on that feature.
12. Switch to the demographic branch
```git
git checkout demographic
```

## Scenario #2
Let's walk through the Git commands that go along with each step in the scenario you just observed in the video.

### Step 1: You check your commit history, seeing messages about the changes you made and how well the code performed.

1. View the log history
```git
git log
```

### Step 2: The model at this commit seemed to score the highest, so you decide to take a look.
2.Check out a commit
```git
git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560
```

After inspecting your code, you realize what modifications made it perform well, and use those for your model.

### Step 3: Now, you're confident merging your changes back into the development branch and pushing the updated recommendation engine.
3. Switch to the develop branch
```git
git checkout develop
```

4. Merge the friend_groups branch into the develop branch
```git
git merge --no-ff friend_groups
```
5. Push your changes to the remote repository
```git
git push origin develop
```