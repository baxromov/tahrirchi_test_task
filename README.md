# tahrirchi_test_task
## Some questions for reasoning:
1. How would you automate this process so that we can get new datasets every day?
Answer: 
  For this question, I am got at in DevOps. So, Solution is We should write cron 
job for `start_process.sh` in particular time and every day the cron job works automaticaly
and run `start_process.sh`.

2. What file format would you use to store this data?
Answer:
  In the saving process the file created with `.csv` file format

3. How would you evaluate the quality of the collected data?
Answer:
  I would evaluate normal data.
 

`HINT`: If you use unix system, you can jus run the `start_process.sh`

Example: 
```bash
chmod +x start_process.sh

```

```bash
./start_process.sh
```
