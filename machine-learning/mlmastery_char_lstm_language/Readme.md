https://machinelearningmastery.com/develop-character-based-neural-language-model-keras/

Why are we not encoding the chars to ASCII values? That would be more predictable.

refs:

https://github.com/fchollet/keras/issues/3548


```
Input: Sing a son
Sing a song of sixpence, A poc
Input: king was i
king was in his counting house
Input: hello worl
hello worlb ee  cakrinnt aa ba
```
