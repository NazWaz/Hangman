# Hangman

The project consists of a tool that allows the user to play the popular word guessing game, Hangman. It was built using Python in VS Code and required me to learn and understand the basic fundamentals of Python as well as proper coding practices such as the use of GitHub and this documentation to record all changes and what I have learnt throughout the process.


# Milestone 1

The first step was to set up the dev environment and ensure that the files were being backed up using Github.    

# Github

![](Documentation/1/1.png)

- The first line of the code was to create this actual md file using `echo "# hangman" >> README.md`. Then using `git init`, the connection between the code on my PC and my github was initialised, after also including my email and username. The md file was then staged using the `git add` command and once this was staged, it was ready to be committed using the `git commit -m` command. Though I used this initially for commits, I learnt to also use the source control tab to quickly stage and commit changes. 

- The `git branch -M main` command allowed me to rename the master (main) branch to main for clarity and I learnt to make additional branches using the `git checkout -b` command followed by the branch name. This was important to learn as all future changes to the code needed to be kept away from the main branch of code until it was checked making it easy to identify changes and errors. 

- After changes were made on any branches, I had to use `git checkout main` to return to the main branch and merge the new branch back to the main branch using `git merge` followed by the new branch name. I could constantly check which branch I was on as well as the staged changes using `git status`. Once merged, I could upload the changes to the main branch to Github using `git push -u origin main` however i first used the command `git remote add origin` once to ensure that all the changes were going through correctly to the repository.

# Miniconda

- After installing miniconda, the dev environment in VS Code had to be set up properly. First, the version was checked to see if it was installed or up to date using `conda --version`. Then it was initialised using `conda init` and to ensure it was initialised in the correct state on startup and using bash, `conda init bash` was used. To begin setting up the environment, I used `conda create -n hangman` to create a new environment called hangman and after agreeing to the set up I was able to use `conda activate` to complete the set up.

- I could check the library of the environment to see what was installed using `conda list` and the aim was to install pip to this environment, to easily install even more libraries. `which pip` allowed me to check the path of the pip in use and since the current hangman environment was missing pip, `conda install pip` was used to install it here. Finally, `pip install` was used to install any essential libraries, so I used `pip install ipykernel`.


# Milestone 2

The second milestone involved creating the variables for the game. 

![](Documentation/2/1.png)

- My first task here was to create a list of random fruits. I named the list `word_list` and assigned values inside using an `=` and a pair of square brackets `[]`. For the list, each fruit had to be put inside quotation marks `" "` so they would be recognised as strings, their data type. Each fruit's name was seperated by a comma `,` and once the list was created it could then be output using the `print()` function. Here `print(word_list)` outputs the list of fruits I created.

- The first line of code was important as a hashtag `#` is used to indicate that it is not part of the code and is instead a comment. However, in VS Code specifically, the `# %%` has a special feature where it creates a magic cell. Essentially this allows the block of code following it to be run independently instead of running the full code, making the process much easier. Of course comments were added to the code also to help keep track.

- The second line of code was also important for a later function. Though it was not used in this block with the list, the `import` function was used to import one of Python's built-in modules, the random module.

![](Documentation/2/2.png)

- This next block of code was used to choose a random word from the list of fruits I created. This was done by using the function `random.choice()` with the list `word_list` and assigning it to the variable called `word`. Then this word was printed using `print(word)` and this cell was ran by pressing Shift + Enter together and checked by seeing whether the output would give random words from the list more than once.

![](Documentation/2/3.png)

- The final block of code allowed the user to input a single letter as a guess. `input()` is used with a message `"Enter a single letter"` and assigned to the variable `guess` to give the user a prompt when the code is run, to enter their guess. This guess was also printed.

- An if-else loop was used to check the validity of the guess, that it was both a single character and from the alphabet. The code began with `if` and then the conditions followed. The length was checked using `len()` function and `.isalpha()` was used to check that the character is an actual letter. After these 2 conditions, a colon was used and the indented code was what happens should both conditions be true. In this case, if the guess was a single letter, the message `"Good guess!"` would be output to the user.

- The `else` function provided the alternative outcome, should the `if` condition not be fulfilled. So if the character was more than 1 or a number for example, a different message would be printed: `"Oops! That is not a valid input."`.


# Milestone 3


# Milestone 4


# Milestone 5