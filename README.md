Rangesearch-box
==============

Rangesearch-box is a algorithm performing range search queries.<br>
Not pretending to be optimal or more flexible than other solutions,<br>
but rather an experiment of a non tree based rangesearch algorithm.

## Algorithm
The overall idea is to sort the points according to each dimension and index them.<br>
We can then apply some efficient search algorithm in the sorted arrays <br>
The intersection of indexes on each dimension will finally provide the boxes.

## Visually speaking


## Formally speaking
Let:

![](https://raw.githubusercontent.com/pelodelfuego/rangesearch-box/master/img/formal_def.gif)

## Conclusion

We successfully created a rangesearch algorithm which does not rely on tree structure.

The big drawback of this approach is the constraints on the boxes take a big assumption: only one shape available.

However the performances of this approach are quite good for a python/numpy implementation.
Faster than sklearn Balltree (in cython) with a python metric (which is a bottle neck) ~x25.
More details in the demo notebook.

We can also note that is scales properly with the number of dimension (perf-wise)

It was a funny experiment though =)
Could be interesting to implement in cython.
