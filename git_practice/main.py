from add_lists import add_lists

if __name__ == "__main__":
    result = add_lists(['wel', 't', 'r'], ['come', 'o', 'os'])
    print(result)

import list_ops as lo

if __name__ == "__main__":
    foo = [1,2,3]
    bar = [4,5,6]
    print("foo+bar=", lo.add(foo, bar))
    print("foo-bar=", lo.subtract(foo, bar))
    print("foo*bar=", lo.multiply(foo, bar))
    print("foo/bar=", lo.divide(foo, bar))
