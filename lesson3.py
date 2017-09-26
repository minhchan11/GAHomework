
n Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

file_nested_list = pd.read_table('chipotle.tsv')
file_nested_list.head()

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

header = file_nested_list.columns
data = pd.read_table('chipotle.tsv', header=None)

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps and then code each step
'''
df['item_price'] = df['item_price'].map(lambda x: float(x.replace('$','')))
df.pivot_table(values='item_price', index='order_id', aggfunc=np.mean)


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
list(df[df['item_name'] == 'Canned Soda']['choice_description'].unique())

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

dfBurrito['total_toppings'] = dfBurrito.apply(lambda x: len(x['choice_description'].replace(']','').replace('[','').split(',')), axis=1)
dfBurrito['total_toppings'].mean()

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
dfChips = df[df['item_name'].str.contains('Chips')].groupby('item_name').sum().reset_index()
dfChips[['item_name','quantity']].set_index('item_name')['quantity'].to_dict()
'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

#[your code here]

