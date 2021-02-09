# Constraint Satisfaction Exercise

Use your knowledge of solving constraint satisfaction problems to answer questions on a multiple-choice test.  

## Questions

1. Which pokemon is the slowest?    &nbsp;&nbsp;&nbsp; A, B, C, D, E
1. Which pokemon is the heaviest?   &nbsp;&nbsp; A, B, C, D, E
1. Which pokemon is the shortest?   &nbsp;&nbsp; A, B, C, D, E
1. Which pokemon is the fastest?    &nbsp;&nbsp;&nbsp;&nbsp; A, B, C, D, E
1. Which pokemon is the footprint?  &nbsp; A, B, C, D, E

## Constraints

Here is what we know about each pokemon and their domains.

* 1 cannot be D
* 2, 3 and 4 cannot be A or E
* 5 cannot be D or E

_Fill out the domain table of possible values for each pokemon._

| Pokemon | A | B | C | D | E |
|---------|---|---|---|---|---|
| 1       | A  | B  |  C |   |  E |
| 2       |   |  B | C  | D  |   |
| 3       |   |  B | C  | D  |   |
| 4       |   |  B | C  | D  |   |
| 5       | A  | B  | C  |   |   |

We also know that:

* The fastest pokemon cannot be the slowest.
* The heaviest pokemon is the slowest.
* The shortest pokemon is neither the heaviest nor the fastest.
* The footprint belongs to the fastest pokemon.

_Draw the constraint graph._

![pokemon constraint graph](images/csp-pokemon-solution.png)

_Which pokemon is the most constrained?_ &nbsp; 1, 2, 3, __4__, 5

## Searching for Answers

Find answers to the questions that are consistent with the constraints by constructing a search tree.  Making sure that you:

* Assign answers to question while not violating any constraints.
* Know that some questions can have the same answer.
* Search in numeric order.

_Use __Depth First Search__ only check constraints after assignment and do not perform constraint propagation._

![pokemon dfs and dfs search trees](./images/pokemon-dfs-solution.jpg)


_Then try it again with __DFS + Forward Checking__ where you remove incompatible neighboring values after assignment._

![pokemon dfs and dfs+fc search trees](./images/pokemon-dfs+fc-solution.jpg)

_Finally, use the assignments from your search to answer the questions 1 to 5 above._

## Answers

| Pokemon | DFS Answer | DFS + FC Answer |
|---------|---|---|
| Which pokemon is the slowest?       | B | B |
| Which pokemon is the heaviest?      | B | B |
| Which pokemon is the shortest?      | D | D |
| Which pokemon is the fastest?       | C | C |
| Which pokemon is the footprint?     | C | C |

_Note: Here the answers are the same for both methods but this is not guaranteed._
