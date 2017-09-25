## Lesson 4 Homework: Command Line Chipotle

#### Submitting Your Homework

* Create a Markdown file that includes your answers **and** the code you used to arrive at those answers.
* Add this Markdown file to a GitHub repo that you'll use for all of your coursework.
* Submit a link to your repo using the homework submission form listed just below the course schedule on the class repo on the main README.md page. [(submission form)](https://docs.google.com/forms/d/e/1FAIpQLScH_m8Le4w0sqsvm5uNOTd08p4KDTW8WgnWVP1kFf4CCBi2Ow/viewform)

#### Command Line Tasks

1. Look at the head and the tail of **chipotle.tsv** in the **data** subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

Answer:
head chipotle.tsv
tail chipotle.tsv

Each row is a separate item that is ordered, grouped by id and each column is its attributes

order_id: id of each orders
quantity: quantity of each item
item_name: name of item ordered
choice_description: ingredients
item_price: price of each item
2. How many orders do there appear to be?
cut -f1 chipotle.tsv | uniq
There are 1834 orders

3. How many lines are in this file?
wc -l chipotle.tsv
There are 4623 lines

4. Which burrito is more popular, steak or chicken?
grep 'Steak Burrito' chipotle.tsv | wc -l
grep 'Chicken Burrito' chipotle.tsv | wc -l

Chicken (553) is more popular than Steak (368)

5. Do chicken burritos more often have black beans or pinto beans?
grep 'Chicken Burrito' chipotle.tsv | grep 'Black Beans'|wc -l
grep 'Chicken Burrito' chipotle.tsv | grep 'Pinto Beans'|wc -l

More black beans (282) than pinto beans (105)

6. Make a list of all of the CSV or TSV files in the [our class repo] (https://github.com/ga-students/DS-SEA-3). repo (using a single command). You will be working on your local repo on your laptop.  Think about how wildcard characters can help you with this task.

find . -name &#42;.&#42;sv

7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files of [our class repo] (https://github.com/ga-students/DS-SEA-3).

grep -r -i 'dictionary' . | wc -l

55 times

8. **Optional:** Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!
cut -f1,2 chipotle.tsv | uniq | sort -nk 2 |tail -1
The order with the largest numbers of items is order number 1443

