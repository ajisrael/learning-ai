# Notes

## Phase 0

### Milestone 0.2

#### Task 0.2.2 - make a broadcast fail on purpose and read the error message

Error message to look out for on broadcast:

```bash
Traceback (most recent call last):
  File "/home/ajisrael/learning/learning-ai/projects/phase-0/milestone-0.2/example_numpy.py", line 46, in <module>
    print("\narr + row (broadcast) =\n", arr + row)
                                         ~~~~^~~~~
ValueError: operands could not be broadcast together with shapes (3,4) (5,)
```
