name: Cleanup

on:
  schedule:
  - cron: '0 0 * * *'

jobs:
  run_cleanup:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - run: ./cleanup-script.sh
