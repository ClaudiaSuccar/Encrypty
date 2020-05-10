# Encrypty
A program that lets you encrypt a message.

1. The program stores an array that holds the characters in the alphabet.
2. Slicing is used to access the array and reverse it.
```python
r = alphabet[::1]
```
3. The user inputs their message and the message is split into a list.

```python
message = 'hello'
split = list(message)
print(message)

['h','e','l','l','o']

```
4. The message is then thrown into a for loop, where it is converted to the encrypted message.
```python
for i in split:
  index = alphabet.index(i)
  new_letter = r[index]
  print(new_letter)
```
- The index of i in alphabet is stored in index `index = alphabet.index(i)`.
- new_letter is assigned to the position of index in the reversed alphabet `new_letter = r[index]`.
5. The encrypted message is printed to the user.
```python
print(new_letter)

s
v
o
o
l
```
