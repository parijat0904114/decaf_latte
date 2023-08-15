name: Comment on issue

on:
  issues:
    types: [labeled]

jobs:
  comment:
    runs-on: ubuntu-latest
    if: github.event.label.name == 'thumbs up'
    steps:
    - name: Add comment
      uses: actions/github-script@v3
      with:
        script: |
          github.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: "Thanks for your thumbs up! :+1. I appreciate it"
          });
