"""
Given a list of full paths to files, and a list of filenames to query,
report all the full paths that match that filename.

Example input:

```python
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
```

Example return value:

```
[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
"""

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # create dict
    file_dict = dict()

    # filename as keys, full paths as values
    for file in files:
        filename = file.split('/')[-1]
        if filename not in file_dict:
            file_dict[filename] = []
        file_dict[filename].append(file)

    # loop through files
    # nested loop to return all paths matching filename
    result = []
    for query in queries:
        if query in file_dict:
            for file in file_dict[query]:
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
