# Advanced Template for Math Homework

You are going to create a new repo called https://github.com/your_github_id/math.

Example: _github.com/vishalapte/math_

```shell
math
├── score.py
├── math001
│   ├── README.md
│   └── solution.py
├── math002
│   ├── README.md
│   └── solution.py
├── math003
│   ├── README.md
│   └── solution.py
├── math004
│   ├── README.md
│   └── solution.py
├── ...
└── math020
    ├── README.md
    └── solution.py
```

The solution to every problem so far (20) and all future problems are going to be stored in this repo.

## 1. Consolidate all solutions under a single repo

Take all the assignments you have done and populate the directories under math as follows:

1. Create a directory for the math assignment named mathXXX (example: math001) where XXX is a zero-padded problem number
2. Copy the README.md from the problem statement to the mathXXX directory
3. Consolidate your answers from answer.py and solver.py into a single file called solution.py

Do this for all 20 assignments.

Publish the repo to github so that the trainers can see it.

## 2. Write a framework to test solutions to all math problems

Write a script in math/score.py that will test `answer()` and `solver()` for every problem (math000) directory thus far and in the future.
