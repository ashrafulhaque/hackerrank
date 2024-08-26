# Python

Owner: Md. Ashraful Haque
Tags: Codebase

<aside>
💡 Python is a high-level, general-purpose programming language.  Python **is** used for web and software development, task automation, machine learning, data science, financial analysis, and artificial intelligence etc.

</aside>

## Python Language Basics

---

- ***Data Types***
    
    This is how you assign a value to a variable for various data types in [python. No](http://python.No) explicit data type declaration like C and Java:
    
    | Example | Data Type |
    | --- | --- |
    | x = "Hello World" | str |
    | x = 20 | int |
    | x = 20.5 | float |
    | x = 1j | complex |
    | x = ["apple", "banana", "cherry"] | list |
    | x = ("apple", "banana", "cherry") | tuple |
    | x = range(6) | range |
    | x = {"name" : "John", "age" : 36} | dict |
    | x = {"apple", "banana", "cherry"} | set |
    | x = True | bool |
    | x = None | NoneType |
    
- ***Conditions***
    
    ```python
    age = int(input())
    
    if age <= 12:    # note that, condition block starts with ( : )
        print("Junior")  
    elif age in range(13,20):   # note that, python calls it ( elif ) instead of else if
        print("Teenager")
    elif age >= 20 and age <= 35: # in python, we use ( and, or ) instead of &&, ||
        print("Young")
    else:
    		print("Senior Citizen!")
    ```
    
- ***Python Lists***
    
    List is a collection which is ordered and changeable. Allows duplicate members.
    
    ```python
    mylist = ["abc", 34, True, 40, "male"]
    
    print(mylist) # prints the whole list
    
    print(len(mylist) # prints the length of the list
    
    print(mylist[1]) # prints the 2nd item of the list as the first item has index 0
    
    print(mylist[-1]) # print the last item of the list
    
    print(mylist[1:4]) # starts at index 1 (included) and ends at index 4(not included)
    
    mylist.append("John") # append method is used To add an item to the end of the list
    
    mylist.insert(1, "Lily") # Insert an item as the second position
    
    # Creating a Multi-Dimensional List by Nesting a List Inside a List)
    list2 = [['apple', 'banana'], ['mango',['orange']]
    
    print(List[0][0]) # Accessing an element from a Multi-Dimensional list
    ```
    
     
    
- ***Python Sets***
    
    Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
    
    ```python
    fruits = {"apple", "banana", "cherry", "apple" }
    
    print(fruits) # this will ignore the duplicate value "apple" 
    
    fruits2 = {"apple", "banana", "cherry", True, 1, False, 0}
    
    print(fruits2) # (True and 1) and (False and 0) is considered same
    
    fruits.add("orange") # adds new item to set fruits
    
    fruits.clear() # remove all elements from the fruits set
    
    newset = fruits.copy() # copy the fruits set into newset
    
    z = x.union(y) # return all items from both sets, duplicates are excluded
    
    z = x.difference(y) # return items that only exist in set x, and not in set y
    
    z = x.intersection(y) # return items that exist in both set x, and set y
    
    z = x.issubset(y) # return True if all items in set x are present in set y
    ```
    
- ***Python Tuples***
    
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    
    ```python
    thistuple = ("apple", "banana", "cherry")
    print(thistuple)
    ```
    
- ***Python Dictionaries***
    
    Dictionaries are used to store data values in key : value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates.
    
    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    
    # We can use the same syntax to add another key, value pair
    car["generation"] = 7
    
    # The in operator tells us whether something is a key in the dictionary
    'model' in car # True
    
    # A for loop over a dictionary will loop over its keys
    for i in car:
        print("{} = {}".format(i, car[i]))
    ```
    
- ***Loops***
    
    **While Loop:** While loop can execute a set of statements as long as a condition is true. The syntax is almost the same as while loop in C, Java or PHP.
    
    ```python
    i = 1
    while i < 6:
      print(i)
      if i == 3:
        break
      i += 1
    ```
    
    F**or Loop:**  A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). It can also iterate for a specific number for a specific range.
    
    ```python
    print("List Iteration") 
    fruits = ["apple", "mango", "orange"] 
    for i in fruits: 
    	print(i) 
    	
    print("\nString Iteration") 
    string = "Bangladesh"
    for i in s: 
    	print(i) 
    	
    print("\nDictionary Iteration") 
    d = dict( 'xyz' = 123, 'abc' = 345)
    for i in d: 
    	print("%s %d" % (i, d[i])) 
    	
    print("\nIteration for a range: ") 
    for i in range(5): 
    	print(i) # prints (0-4) 
    
    ```
    
- ***List Comprehensions***
    
    List comprehensions are one of Python's most beloved and unique features. List comprehension offers a shorter syntax when you want to create a new list. The syntax is 
    
    ```python
    # expression
    list_name = [*expression* for *item* in *iterable* if *condition* == True]
    ```
    
    ```python
    # This will create a list with the values: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    squares = [n**2 for n in range(10)]
    print(squares) 
    
    # This will create a list with the values: [0, 1, 2, 3, 4]
    newlist = [x for x in range(10) if x < 5]  # we can apply conditions inside LC
    
    fruits1 = ["apple", "banana", "cherry", "apple" ]
    fruits2 = [x.upper() for x in fruits1] # Set the values in list2 to upper case
    ```
    
- ***Strings***
    
    Strings in Python can be defined using either single or double quotations. They are functionally equivalent. Strings are *immutable*. We can't modify them.
    
    ```python
    x = "Pluto is a planet" # string using single quotation
    y = 'Pluto is a planet' # string using double quotation
    
    s = 'What\'s up?'	# escaping single quote character inside a single-quoted str
    
    """ The print() function automatically adds a newline character unless we specify a value for the keyword argument end other than the default value of '\n': """
    
    print("Hello", end='')
    print("World")  # "Hello World" gets printed on single line
    
    planet = 'Pluto'
    l = [char+'! ' for char in planet] # ['P! ', 'l! ', 'u! ', 't! ', 'o! ']
    
    # String Methods
    planet.upper() # PLUTO
    planet.lower() # pluto
    
    planet.index("uto") # Searching for the first index of a substring (2)
    planet..startswith("P") # True
    
    txt = "Bangladesh is beautiful"
    # Turn a string into a list of smaller strings, breaking on whitespace by default
    words = txt.split() # ['Bangladesh ', 'is', 'beautiful']
    
    datestr = '1956-01-31'
    year, month, day = datestr.split('-') # split on something (-) other than whitespace
    
    # str.join() takes us in the other direction, joining a list of strings up into one long string, using the string it was called on as a separator.
    
    '/'.join([month, day, year]) # '01/31/1956'
    
    planet = "Earth"
    position = 3
    
    concat1 = planet + " is beautiful" # concatenate strings with the + operator
    
    # we must convert numbers into str() before concatanation
    concat2 = planet + " ,your position from SUN is " + str(position) 
    
    # we can use format to 
    concat3 = "{}, you'll always be the {}th planet to me.".format(planet, position)
    ```
    
- **Regular Expressions**
    
    A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. Python has a built-in package called `re`, which can be used to work with Regular Expressions. Details of Python RegEx: 
    
    ```python
    import re
    
    # Search the string to see if it starts with "The" and ends with "Spain"
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt) # matches "The rain in Spain"
    
    # String can start with +, - or . symbol
    # String must have at least 1 decimal value 
    # String must have one . symbol and can be converted to float 
    txt2 = +1.23 
    match = re.search(r"^[+-]?\d*\.\d+$",txt2) 
    ```
    
    [Python RegEx](https://www.w3schools.com/python/python_regex.asp)
    
- **Itertools**
    
    ## Itertools
    
    The `itertools` module in Python provides a collection of tools for handling iterators. It is a standard library module that contains numerous functions to work with iterators, making it easier to create complex iterators. Here are some commonly used functions from the `itertools` module:
    
    ### `count()`
    
    Returns an iterator that generates consecutive integers, starting from a specified number.
    
    ```python
    import itertools
    
    counter = itertools.count(start=0, step=1)
    print(next(counter))  # Output: 0
    print(next(counter))  # Output: 1
    
    ```
    
    ### `cycle()`
    
    Returns an iterator that cycles through an iterable indefinitely.
    
    ```python
    import itertools
    
    cycler = itertools.cycle(['A', 'B', 'C'])
    print(next(cycler))  # Output: A
    print(next(cycler))  # Output: B
    print(next(cycler))  # Output: C
    print(next(cycler))  # Output: A (repeats)
    
    ```
    
    ### `chain()`
    
    Combines multiple iterables into a single iterator.
    
    ```python
    import itertools
    
    combined = itertools.chain([1, 2, 3], ['a', 'b', 'c'])
    print(list(combined))  # Output: [1, 2, 3, 'a', 'b', 'c']
    
    ```
    
    ### `combinations()`
    
    Generates all possible combinations of a specified length from the input iterable. Note that, a combination does not consider any repeated value group.
    
    ```python
    import itertools
    
    combos = itertools.combinations('ABC', 2)
    print(list(combos))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
    
    ```
    
    ### `permutations()`
    
    Generates all possible permutations of a specified length from the input iterable.
    
    ```python
    import itertools
    
    perms = itertools.permutations('ABC', 2)
    print(list(perms))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    
    ```
    
    ### `product()`
    
    Generates the Cartesian product of input iterables.
    
    ```python
    import itertools
    
    prod = itertools.product([1, 2], ['a', 'b'])
    print(list(prod))  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
    
    ```
    
    ### `groupby()`
    
    Groups elements of an iterable based on a specified key function.
    
    ```python
    import itertools
    
    data = [{'name': 'A', 'group': 1}, {'name': 'B', 'group': 1}, {'name': 'C', 'group': 2}]
    data = sorted(data, key=lambda x: x['group'])
    grouped = itertools.groupby(data, key=lambda x: x['group'])
    
    for key, group in grouped:
        print(key, list(group))
    # Output:
    # 1 [{'name': 'A', 'group': 1}, {'name': 'B', 'group': 1}]
    # 2 [{'name': 'C', 'group': 2}]
    
    ```
    
    These are just a few of the many functions available in the `itertools` module. Each function provides a unique way to handle iterators, making your code more efficient and easier to read.
    
- Collections
    
    ### Collections
    
    The collections module in Python provides specialized container datatypes as alternatives to Python's general purpose built-in containers like dict, list, set, and tuple. These specialized datatypes offer additional functionality and optimization for specific use cases.
    
    ### Counter()
    
    Counter is a dict subclass for counting hashable objects. It's a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    
    ```python
    from collections import Counter
    
    # Count occurrences of elements in a list
    my_list = [1, 1, 2, 3, 3, 3, 4]
    count = Counter(my_list)
    print(count)  # Output: Counter({3: 3, 1: 2, 2: 1, 4: 1})
    
    # Find the two most common elements
    print(count.most_common(2))  # Output: [(3, 3), (1, 2)]
    ```
    
    ### defaultdict()
    
    defaultdict is a dictionary subclass that calls a factory function to supply missing values, instead of raising a KeyError.
    
    ```python
    from collections import defaultdict
    
    # Create a defaultdict with default value as list
    dd_list = defaultdict(list)
    
    # Adding elements to the defaultdict
    dd_list['fruits'].append('apple')
    dd_list['fruits'].append('banana')
    dd_list['vegetables'].append('carrot')
    
    print("defaultdict with list as default_factory:")
    print(dd_list)
    print("Accessing a non-existent key 'grains':", dd_list['grains'])
    
    # Output:
    # defaultdict with list as default_factory:
    # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})
    # Accessing a non-existent key 'grains': []
    
    # Create a defaultdict with default value as int
    dd_int = defaultdict(int)
    
    # Incrementing counts
    dd_int['apple'] += 1
    dd_int['banana'] += 2
    dd_int['apple'] += 3
    
    print("\ndefaultdict with int as default_factory:")
    print(dd_int)
    print("Accessing a non-existent key 'cherry':", dd_int['cherry'])
    
    # Output:
    # defaultdict with int as default_factory:
    # defaultdict(<class 'int'>, {'apple': 4, 'banana': 2})
    # Accessing a non-existent key 'cherry': 0
    
    # Create a defaultdict with a custom default_factory
    def default_value():
        return "Unknown"
    
    dd_custom = defaultdict(default_value)
    
    dd_custom['name'] = "John"
    print("\ndefaultdict with custom default_factory:")
    print(dd_custom['name'])
    print("Accessing a non-existent key 'age':", dd_custom['age'])
    
    # Output:
    # defaultdict with custom default_factory:
    # John
    # Accessing a non-existent key 'age': Unknown
    ```
    
    ### namedtuple()
    
    namedtuple creates tuple subclasses with named fields, providing a convenient way to create small immutable data structures.
    
    ```python
    from collections import namedtuple
    
    # Create a namedtuple type called Point
    Point = namedtuple('Point', ['x', 'y'])
    
    p = Point(11, y=22)
    print(p[0] + p[1])  # Output: 33
    print(p.x + p.y)    # Output: 33
    print(p)            # Output: Point(x=11, y=22)
    ```
    
    ### OrderedDict()
    
    OrderedDict is a dict subclass that remembers the order in which keys were inserted. As of Python 3.7+, the built-in dict class maintains insertion order by default, but OrderedDict still offers some additional functionality.
    
    ```python
    from collections import OrderedDict
    
    # Creating an OrderedDict
    od = OrderedDict()
    od['apple'] = 1
    od['banana'] = 2
    od['cherry'] = 3
    od['date'] = 4
    
    print("Original OrderedDict:")
    print(od)
    # Output: OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3), ('date', 4)])
    
    # Moving an existing key to the end
    od.move_to_end('banana')
    print("\nAfter moving 'banana' to the end:")
    print(od)
    # Output: OrderedDict([('apple', 1), ('cherry', 3), ('date', 4), ('banana', 2)])
    
    # Moving an existing key to the beginning
    od.move_to_end('cherry', last=False)
    print("\nAfter moving 'cherry' to the beginning:")
    print(od)
    # Output: OrderedDict([('cherry', 3), ('apple', 1), ('date', 4), ('banana', 2)])
    
    # Deleting and re-inserting the same key
    del od['apple']
    od['apple'] = 5
    print("\nAfter deleting and re-inserting 'apple':")
    print(od)
    # Output: OrderedDict([('cherry', 3), ('date', 4), ('banana', 2), ('apple', 5)])
    
    # Using OrderedDict for a simple cache
    class SimpleCache(OrderedDict):
        def __init__(self, capacity):
            super().__init__()
            self.capacity = capacity
    
        def get(self, key):
            if key not in self:
                return None
            self.move_to_end(key)
            return self[key]
    
        def put(self, key, value):
            if key in self:
                self.move_to_end(key)
            self[key] = value
            if len(self) > self.capacity:
                oldest = next(iter(self))
                del self[oldest]
    
    # Using the SimpleCache
    cache = SimpleCache(3)
    cache.put('A', 1)
    cache.put('B', 2)
    cache.put('C', 3)
    print("\nInitial cache:")
    print(cache)
    # Output: OrderedDict([('A', 1), ('B', 2), ('C', 3)])
    
    cache.put('D', 4)  # This will remove 'A' as it's the oldest item
    print("\nCache after adding 'D':")
    print(cache)
    # Output: OrderedDict([('B', 2), ('C', 3), ('D', 4)])
    
    cache.get('B')  # This will move 'B' to the end
    print("\nCache after accessing 'B':")
    print(cache)
    # Output: OrderedDict([('C', 3), ('D', 4), ('B', 2)])
    ```
    
    ### deque()
    
    deque (double-ended queue) is a list-like container with fast appends and pops on either end. It's especially useful for implementing queues and breadth-first tree searches.
    
    ```python
    from collections import deque
    
    d = deque(['a', 'b', 'c'])
    d.append('d')        # Add to right
    d.appendleft('e')    # Add to left
    
    print(d)  # Output: deque(['e', 'a', 'b', 'c', 'd'])
    
    print(d.pop())        # Remove from right: 'd'
    print(d.popleft())    # Remove from left: 'e'
    
    print(d)  # Output: deque(['a', 'b', 'c'])
    ```
    
- Date and Time
    
    ### Calendar Module
    
    The calendar module in Python provides functions for working with calendars, including methods to format calendar output and determine various calendar-related information. Here are some of the most important methods and arrays in the calendar module:
    
    ### Important Methods
    
    - **weekday(year, month, day)**
        
        Returns the day of the week as an integer (0-6), where Monday is 0 and Sunday is 6.
        
        ```python
        import calendar
        
        # Get the day of the week for a specific date
        print(calendar.weekday(2024, 8, 26))  # Output: 0 (Monday)
        print(calendar.weekday(2024, 12, 25))  # Output: 2 (Wednesday)
        ```
        
    - **monthcalendar(year, month)**
        
        Returns a matrix representing a month's calendar. Each row represents a week; days outside of the month are represented by zeros.
        
        ```python
        import calendar
        
        # Get the calendar for August 2024
        august_2024 = calendar.monthcalendar(2024, 8)
        print(august_2024)
        # Output: 
        # [[0, 0, 0, 1, 2, 3, 4], 
        #  [5, 6, 7, 8, 9, 10, 11], 
        #  [12, 13, 14, 15, 16, 17, 18], 
        #  [19, 20, 21, 22, 23, 24, 25], 
        #  [26, 27, 28, 29, 30, 31, 0]]
        
        # Access a specific day (e.g., August 15, 2024)
        print(august_2024[2][3])  # Output: 15
        ```
        
    - **isleap(year)**
        
        Returns True for leap years, False for non-leap years.
        
        ```python
        import calendar
        
        print(calendar.isleap(2024))  # Output: True
        print(calendar.isleap(2025))  # Output: False
        ```
        
    
    ### Important Arrays
    
    - **day_name**
        
        An array that represents the names of the days of the week.
        
        ```python
        import calendar
        
        # Print all day names
        for day in calendar.day_name:
            print(day)
        
        # Output:
        # Monday
        # Tuesday
        # Wednesday
        # Thursday
        # Friday
        # Saturday
        # Sunday
        
        # Get a specific day name
        print(calendar.day_name[0])  # Output: Monday
        print(calendar.day_name[6])  # Output: Sunday
        ```
        
    - **month_name**
        
        An array that represents the names of the months of the year. Note that the first element is an empty string, as month numbering starts from 1.
        
        ```python
        import calendar
        
        # Print all month names
        for month in calendar.month_name[1:]:  # Skip the first empty element
            print(month)
        
        # Output:
        # January
        # February
        # ...
        # December
        
        # Get a specific month name
        print(calendar.month_name[1])   # Output: January
        print(calendar.month_name[12])  # Output: December
        ```
        
    
    These methods and arrays provide powerful tools for working with dates and calendars in Python, allowing you to perform various calendar-related operations efficiently.