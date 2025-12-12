# Basic Documentation

___

## Table of Contents
1. [Git Commands](#git-commands)
	1. [General Commands](#general-commands)
	2. [Branches](#branches)
	3. [Checkout](#checkout)
	4. [Stashing](#stashing)
2. [GitHub Setup](#github-setup)
	1. [Documentation and Information](#documentation-and-information)
	2. [What to do in Git Bash](#what-to-do-in-git-bash)
	3. [What to do on GitHub](#what-to-do-on-github)
3. [GitHub](#github)
	1. [Git Remote](#git-remote)
	2. [Git Push](#git-push)
	3. [Git Pull](#git-pull)
4. [Simple Git Workflow](#simple-git-workflow)
5. [Open-source Workflow](#open-source-workflow)
6. [Markdown File Syntax for GitHub](#markdown-file-syntax-for-github)
	1. [Heading Syntax](#heading-syntax)
	2. [Paragraph Syntax](#paragraph-syntax)
	3. [Emphasis Syntax](#emphasis-syntax)
	4. [Blockquotes Syntax](#blockquotes-syntax)
	5. [List Syntax](#list-syntax)
	6. [Escape Characters](#escape-characters)
	7. [Code and Code Blocks Syntax](#code-and-code-blocks-syntax)
	8. [Horizontal Rules](#horizontal-rules)
	9. [Links Syntax](#links-syntax)
	10. [Images Syntax](#images-syntax)
	11. [Tables Syntax](#tables-syntax)
	12. [Footnotes Syntax](#footnotes-syntax)
	13. [View Markdown File Without Commiting](#view-markdown-file-without-commiting)
7. [Sources](#sources)

___

## Git Commands

### General Commands

* `cd folderpath`
	* will load the folder into the command prompt
	* replace folderpath with `..` to go to the previous folder
* `ls`
	* will show what folders are loaded
	* `ls -la`
		* will show the hidden folders
* `pwd`
	* will show the present working directory \(full file path\)
* `mkdir directoryone (directoryect)`
	* will make a new directory or more than one
	* directory is the same thing as folder
* `git mv old_name new_name`
	* will change the name of a directory or file and keep track of the history
* `git --version`
	* check what version of git that you are running
* `git status`
	* check witch files are being tracked by git
* `git init`
	* will initialize git so you can start to track files
* `touch filename.ext (filenameect.ext)`
	* will make a new file in present working directory
* `git add filename.ext (filenameect.ext)`
	* add specific files so they are ready to be commited
	* `git add .`
		* adds all files in present working directory so they are ready to be commited, ignores files listed in \.gitignore file
* `git commit -m "commit message"`
	* requires a commit message
	* commits all staged files \(files that you ran `git add` on\)
	* do one thing per commit
* `git log`
	* shows what commits have happened and when they happend
	* `git log --oneline`
		* shortens the logs to one line each commit
* `.gitignore` file
	* file that has the path for sensitive files that you do not want git to track
* `git diff commitid1..commitid2`
	* will give the differences between two versions of the same file
	* `---` represents what was in commitid1
	* `+++` represents what was in commitid2

### Branches

* `git branch`
	* shows what branches there are
	* marks the branch that you are currently on with \*
* `git branch -m newbranchname`
	* renames the current branch
* `git branch branchname`
	* makes a new branch
* `git checkout branchname`
	* allows you to go on to branchname
	* `git checkout -b branchname`
		* makes a new branch and puts you on the new branch
* `git switch branchname`
	* allows you to go on to branchname
	* `git switch -c branchname`
		* makes a new branch and puts you on the new branch
* `git merge branchname -m "commit message"
	* will merge the branchname with the branch that you are currently on
	* if there are conflicts, it will add markers
	* after all conflicts are resolved, remove the markers

### Checkout

* `git checkout branchname`
	* will allow you to work on branchname
* `git switch branchname`
	* will allow you to work on branchname
* `git checkout HEAD~#`
	* will allow you to look at the commit # prior
* `git checkout commitid`
	* will allow you to go back to a previous commit
* `git switch main/master`
	* will allow you to go back to the most recent commit
* `git reflog`
	* will allow you to go back to the last position of your head
* `git restore filename`
	* will permanently go back to the previous commit
	

### Stashing

* `git stash`
	* allows you to switch branches without commiting
	* will save your changes temporailly
	* saved changes can be loaded into any branch
* `git stash pop`
	* will apply the changes of the most recent stash
	* `git stash pop stash@{#}`
		* will apply the changes of the stash labeled stash@\{\#\}
	* will remove the changes from the stash
* `git stash list`
	* will list all of the changes that are currently stashed
* `git stash apply`
	* will apply the changes of the most recent stash
	* `git stash apply stash@{#}`
		* will apply the changes of the stash labeled stash@\{\#\}
	* will not remove anything from the stash
* `git stash drop`
	* will remove the most resent stash
	* `git stash drop stash@{#}`
		* will remove the stash labeled stash@\{\#\}
* `git stash clear`
	* will remove everything from the stash
* `git stash branch branchname`
	* will make a new branch from the most recent stash
		* new branches name will be branchname
	* applies the stashed changes to the branch
	* then drops the stash that was applied
	* `git stash branch branchname stash@{#}`
		* same but uses the stash specified

___

## GitHub Setup

### Documentation and Information

* [generating a new ssh key and adding it to the ssh agent][1]
* [adding a new ssh key to your github account][2]

### What to do in Git Bash

1. `git status`
2. `git init`
	* only it the repository has not already been initialized
3. `git add`
4. `git commit`
5. `git branch -M main`
	* renames the master branch to main	

### What to do on GitHub

1. click \+
2. add new repository
3. add repository name
4. add description
5. choose public or private
6. add readme\.md file

___

## GitHub

### Git Remote

* `git remote -v`
	* checks for any remote repositories
* `git remote add name link/url`
	* name is usually orgin
	* get link/url from GitHub
	* allows git to look at remote repository
	* use to add local repository to empty GitHub
	* use to connect to original repository if doing open source work
* `git remote rename oldname newname`
	* renames the remote repository
* `git remote remove name`
	* removes the remote repository from git

### Git Push

* `git push remotename branchname`
	* uploads the local repository to the remote repository
* `git push -u remotename branchname`
	* will setup upstream so that you can just use the command `git push`

### Git Pull

* `git clone link/url`
	* will make a copy of a remote repository that you don't have a local repository of
* `git fetch remoterepositoryname`
	* will allow you to see what changes have been made without merging the changes onto the local repository
* `git pull remoterepositoryname branchname`
	* will apply all the changes that are stored in the remote repository branchname
	* branchname is optional, if no branchname will update the entire local repository to match the remote repository

___

## Simple Git Workflow

1. make a working directory \(folder\)
	1. navigate to the directory in cmd
		* cd directorypath
	2. run `git init`
2. run `git add` on files
3. files are in staging area
4. run `git commit` on files
5. files are in local repository
6. run `git push` on repository

___

## Open-source workflow

* On GitHub
	1. fork the codebase
	2. make changes and track with git
	3. make a pull request
* On git
	1. `git clone link/url`
	2. git workflow 2\-6
	3. `git push`

___

## Markdown File Syntax for GitHub

###	Heading Syntax

* \#\(\#\#\#\#\#\)
	* the more \# symbols the smaller the heading
* \=\=\=\=\=\=\=\=
	* the line directly under the heading
	* the heading will be size one \(the largest heading\)
* \-\-\-\-\-\-\-\-
	* the line directly under the heading
	* the heading will be size two

###	Paragraph Syntax

* normal text without any symbols before
* include an empty line between different paragraphs
* add two spaces to the end of a line if you want a new line, but not a new paragraph

###	Emphasis Syntax

| **bold** | `**text**` | `__text__` |
| :---: | :---: | :---: |
| *italic* | `*text*` | `_text_` |
| ***bold and italic*** | `***text***` | `___text___` |
| ~~strikethrough~~ | `~~text~~` |   |
| <mark>highlight</mark> | `<mark>text</mark>` |   |
| <sub>subscript</sub> | `<sub>text</sub>` |   |
| <sup>superscript</sup> | `<sup>text</sup>` |   |
| <ins>underline</ins> | `<ins>text</ins>` |   |

###	Blockquotes Syntax

* use \> at the begining of the line
* multiple lines that all start with \> will form one blockquote
* you can put blockquotes inside of blockquotes by adding more arrows \(\>\>\)
* put an empty row that starts with \> between each line of the blockquote

> This is a blockquote
>
> This is the second line
>
> > This line starts with \>\>
>
> This is the last line


###	List Syntax

* list with number values
	* can start with any number followed by \.
	* numbers can be in any order
* list with bullets
	* can start with these symbols \*, \-, \+

###	Escape Characters

Use \\ to escape the next character

Characters that can be escaped:

| \\ | \` | \* |
| :---: | :---: | :---: |
| \_ | \{ | \} |
| \[ | \] | \< |
| \> | \( | \) |
| \# | \+ | \- |
| \. | \! | \| |

###	Code and Code Blocks Syntax

* use \` to surround the code
* if the code has \` in it then surround the code with \`\`
* for larger code blocks before the code add \`\`\` coding language
* after the last line of code add a new line with \`\`\`
* another way to make code blocks is to indent the entire section

###	Horizontal Rules

* \*\*\*
* \-\-\-
* \_\_\_
* have at least three symbols on the same line
* keep the line above and below empty

###	Links Syntax

* \[text on screen\]\(url "text when hovering"\)
* \<url\>
* reference link
	* in text
		* \[text on screen\]\[\#\]
	* anywhere in \.md file
		* \[\#\]: url "text when hovering"
* you can format the link by sorrounding the entire link
	* \*\*\[**bold text**\]\(url "text when hovering"\)\*\*
* whenever you have a space in a url replace the space with %20
* whenever you have a \( in a url replace the \( with %28
* whenever you have a \) in a url replace the \) with %29

###	Images Syntax

* \!\[alt text\]\(path or url to image "text when hovering"\)
* linked images
	* \[\!\[alt text\]\(path or url to image "text when hovering"\)\]\(url for link\)

###	Tables Syntax

| first row | headings or any text |   |   |
| :---: | :---: | :--- | ---: |
| second row | :\-\-\-: for center alignment | :\-\-\- for left alignment | \-\-\-: for right alignment |
| third row | more text |   |   |
| sorround columns with \| |   |   |   |

###	Footnotes Syntax

* in text[^footnote]
	* \[^#\] or \[^nospaces\]
* anywhere in \.md file
	* \[^#\]: footnote
	* \[^nospaces\]: footnote
[^footnote]: This is the footnote labeled \[^footnote\]  
	this is also part of the footnote since it was indented  
	you need to add two spaces to the end for it to show up on a new line

### View Markdown File Without Commiting

1. open cmd
2. `grip filepath`
3. open browser
4. go to local host stated in terminal

___

## Sources

* Git/GitHub: <https://www.youtube.com/watch?v=zTjRZNkhiEU>
* Markdown file documentation: <https://www.markdownguide.org/basic-syntax/>
* Markdown file documentation: <https://www.markdownguide.org/extended-syntax/>

___

[1]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[2]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
