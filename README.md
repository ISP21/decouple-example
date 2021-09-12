## Simple Example of Externalizing Data

Externalize the name of the file containing student data.

**Requires**: python-decouple (`pip3 install python-decouple`)

First: run `gitstudents.py`.  It works, but the filename is hardcoded.
Not very maintainable.

Let's improve it:

1. create a file named `.env` containing this:
   ```
   # name of file containing student data
   CSVFILE = "students.csv"
   ```

2. In `gitstudents.py`, add:
   ```python
   from decouple import config
   ```

3. And read the filename from the configuration file (.env):
   ```python
   datafile = config('CSVFILE')
   data = open(datafile)
   ```

4. Run the code.  It should still work.  
   - You can rename the file (and change .env) and it still works -- no need to modify code.

5. Externalize the number of students to print (10).  In `.env` add:
   ```
   count = 10
   ```
   In the Python code:
   ```python
   count = config('count', default=10, cast=int)  
   ```
   `cast=int` means to convert the value to `int`; the default is to return the value as a **string**.

6. Run it.  It should still work.  But now you want to print 20 students.

7. In `.env` change the value of `count` to 20.  Run the code again.  Does it work?

---

Python-decouple Doc: <https://pypi.org/project/python-decouple/>

How to Use Decouple: <https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html>

