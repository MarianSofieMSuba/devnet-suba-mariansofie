# Module 1 — Git & GitHub

**Student:** Marian Sofie M. Suba
**Date:** 9/25/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

---

## Key vocabulary (in your own words)

- repository: is an online hub where developers can upload their files
- commit: is an initial checkpoint to save and keep track of modified files
- branch: is an isolated workplace that lets you modify files without automatically affecting the main branch
- push / pull: push is uploading the files that were committed to the repo while pulls the updated files from the repo
- pull request: is where you ask for your modified files to be reviewed before merging
- merge conflict: only happens when there's more than one branches that modified the same file differently

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

```
I first created a branch by hovering into "Branches" beside main
and went with "new branch" instead of the branch command
because I'm more comfortable seeing it visually so I used that

after some changes into this branch, I used the "git add ." to prepare all of my modified files
then "git commit -m text" before doing the "git push"
I eventually used "git log" to see the commit changes just in case

went over to my main repo and saw the pull request
I first reviewed it before doing a merge pull request
since I didn't get any merge conflicts it's all done
```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

My first mistake was forgetting to input a message description during my git commit

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
