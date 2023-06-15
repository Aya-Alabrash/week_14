# week_14

### Initialise the repo

- In this Assignment i started by creating a project on my local then i needed to Initialise a Git repository for the project by running `git init` which creates a new, empty Git repository in the project directory.

- Then, i configure my Git user information by running the following commands:

```
git config --global user.name "Username"
git config --global user.email "Email"
```

- After that, i added some changes to create new files in my local project and commit my changes using `git add` & `git commit`.

- I created a repository on my github then connected my local repository to the remote repository by the following command:
```
git remote add origin <remote_repository_url>
```
- Finally, pushed my local repository to the remote repository using the command:
```
git push -u origin master
```

### Choosen branching strategy

- In this project i decided to use GitHub Flow branching strategy for many resons like:
  - **Maintaining a Single Version of Code** 
  - **Making Code Changes Multiple Times Per Day**
  - **Small team**

### Implementing features in separate feature branches

- In this project i had to create multiple different branches each to add code implementation.
  - `master` is the default & releasing branch.
  - `feature/add_get_covid_func` to add 'get_covid_cases' functionality.
  - `feature/send_email_func` to add 'send_email' functionality.
  - `feature/add_main_examples` to call my funtions with example calls.
  - `feature/add_README` to initialise README.md file.
  - `doc/update_README` to Update README.md file and add project documentation.

  - For each branch, i added my code then commit it, create a pull-request (PR) from each branch to `master` (destination branch) and lastly merged to my `master` branch after testing the functionalities. 

### Merge issues & Conflicts

- When i was creating my PRs, i was't updating my local branches with my remote changes activly by pulling latest changes, which cause me to face conflicts when i was updating a file from a branch that was out-dated with the latset code version on `master` so i had to `git merge master` to my out-dated branch, resolve my conflicts and push again. 

- I also get a chance to use `git rebase` to apply the changes from one branch onto another branch, resulting in a linear history of my commits.
  - Example: I wanted to rebase `feature/add_main_examples` feature branch onto the `master` branch, so i follow, switch to the feature branch:
  ```
  git checkout "feature/add_main_examples"  #switch to the feature branch.
  git fetch origin master  #fetches the latest changes from the origin/master branch.
  git rebase master  # rebases `feature/add_main_examples` branch on top of those changes.
  ```
  - I had some conflicts, so git pause the rebase process until i resolved the conflicts.
  ```
  git add .  #To add my changes after resolving the conflicts.
  git rebase --continue  #To continue the rebase proccess.
  git push --force origin "feature/add_main_examples"  #To push my changes after resolving the conflicts and make sure the history is been managed correctly (Here --force option was needed cause my rebased branch was already pushed on my remote repository).
  ```
