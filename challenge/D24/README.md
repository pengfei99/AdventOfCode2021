
# Solution 
The entire input is in this form repeated 14 times:

```text
inp w
mul x 0
add x z
mod x 26
div z {a}
add x {b}
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y {c}
mul y x
add z y

```
This in decompiled Python is
```python
w = int(input())
x = int((z % 26) + b != w)
z //= a
z *= 25*x+1
z += (w+c)*x

```

Another thing to note is that **the a is 1 seven times and 26 the other seven times**. In the block where a is 1, b is 
always between 10 and 16. It follows that z //= {a} line is no-op and (z % 26) + b != w is always true. 
So the decompiled code becomes:
```python
w = int(input())
z *= 26
z += w+c

```
So this block of code is "pushing" a digit of w+c in base 26. So to get 0 at the end, we have to "pop" these digits back out using z //= 26 and don't add any more back. Thus, in the lines with a=26, x = int((z % 26) + b != w) must be 0, which means the last pushed digit w_old+c must be equal to w_now-b.

For my particular input, it meant that
```text
I[2]+ 6-14 == I[3]
I[4]+ 9- 7 == I[5]
I[8]+ 1- 7 == I[9]
I[7]+ 3- 8 == I[10]
I[6]+14- 7 == I[11]
I[1]+ 5- 5 == I[12]
I[0]+15-10 == I[13]

```
where I is the array of input.