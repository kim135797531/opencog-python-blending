# Progress summary of this week
* Beautiful version is available in [my wiki](http://wiki.dong-min.kim/GSoC_2015_-_Conceptual_Blending).

## Now
### In Progress
* Detect and improve conflict links in newly blended node.
  * Implement evaluating degree of reasonable fitness using 
   information-theoretic method
  * Try simple PLN inference to see if contradictions are unveiled

### To do
**Think**

* Search for good algorithms to use in each step.

**Study**

* Read the research papers.
 * Goguen, *Mathematical Models of Cognitive Space and Time*
 * Markus, et al, *A computational account of conceptual blending in basic 
  mathematics*

**CodingCodingCoding**

* Push my project to OpenCog repository.

**ETC**

* Design about public API of my project, and make its document.

### Pause
* Try to use Unified Rule Engine, PLN in python.
* Select nodes to blending.
  * Make the waiting queue of ConceptNode
  * Currently queue is not need for blending, because now agent make only one 
   new blended node in each step.
  * It will be useful when optimizing blending agent speed by save candidate 
   cache.
  * (15/06/14) I stopped to making Conceptual Blending with MindAgent design.
   It will be resumed when I finish to making Conceptual Blending API.
* Make the links in newly blended node and correct some attribute value
  * Make correction of value level in each source node.
  * (15/06/14) What does it works for?

## Result
### Done
* Write the mid-term evaluation.
  * When I write the project proposal, I think submitting my codes in mid-term 
   evaluation would be needed, so I planned to little long time to summarize my 
   project. But evaluation was just writing one questionnaire..!
* Design about public API of my project, and make its document.
  * Made a Conceptual Blending Config Format document.
  * Still have to make documentation like Overall Idea, Class & Method 
   description, etc.
* Detect and improve conflict links in newly blended node.
  * Make the 2^k possible blend list

### Fail & Deadline Missed
* (empty
  
### Cancel
* (empty)
