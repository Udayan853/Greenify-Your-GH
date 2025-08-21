# Greenify-Your-GH: A Python Script for a Fuller Contribution Graph

Ever looked at your GitHub contribution graph and wished it had more green squares? Maybe you're starting a new streak, or perhaps you just want to fill in those empty days. `greenify-your-gh` is a straightforward Python script designed to help you do just that.

**Disclaimer:** This tool is intended for fun. It creates dummy commits to fill in your contribution graph. It does not reflect actual work or code contributions. 

## Getting Started

Make sure you have **Python 3.x** and **Git** installed on your system

### 1. Clone this repository to your local machine

```bash
git clone [https://github.com/Udayan853/greenify-your-gh.git](https://github.com/Udayan853/greenify.git)
cd greenify-your-gh
```

### 2. Copy main.py to target repository

### 3. Configure and run the script in following format

```bash
python3 main.py <start_date> <end_date>
```
#### Example
```bash
python3 main.py 2025-01-12 2025-01-30
```
This will create a dummy commit for each day between Jan 1, 2025 to Jan 30 2025

## How it works

The script essentially manipulates the environment variables `GIT_AUTHOR_DATE` and `GIT_COMMITER_DATE` environment variables

For each day starting from `start_date` to `end_date`, the script:
- Calculates the timestamp for that day
- Creates an empty file or appends the timestamp to the existing `sample.py` file
- Adds that file by spawning a subprocess with false environment variables
- Commits it with the message `dummy commit`

## Inspiration

This project is largely inspired by [github-greenifier](https://github.com/caguiclajmg/github-greenifier)\
[Greenify-Your-GH](https://github.com/Udayan853/Greenify-Your-GH) aims to make the tool platform agnostic and also support redistribution of existing commits based on user preferences.
