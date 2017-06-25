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



