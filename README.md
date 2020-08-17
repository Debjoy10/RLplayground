<p align="center">
  <img src="https://user-images.githubusercontent.com/45385843/90400641-65856000-e0ba-11ea-8cc6-da167a4ea047.png" />  
</p>
<p align="center"; font-weight:"bold">
  Trying out different RL algorithms on a simple windy grid-world for practice.
</p>


  
## Grid-World
```
---------------------
| | | | | | | | | | |
---------------------
| | | | | | | | | | |
---------------------
| | | | | | | | | | |                  
---------------------
|*| | | | | | |g| | |  ---> (*) -> Current Position, (g) -> Goal Position
---------------------
| | | | | | | | | | |
---------------------
| | | | | | | | | | |
---------------------
| | | | | | | | | | |              
---------------------                  
 0 0 0 1 1 1 2 2 1 0   ---> Wind Values for each column in positive y direction
```
 ### How To Use:
 Git clone this repository and import as   
 ```from gridworld import gridworld_agent```
 
 #### Initialise your Environment 
 ```env = gridworld_agent(r, c, wind-vector, start, goal, action-mode)```  
 **r**             Grid Rows (int)  
 **c**             Grid Columns (int)  
 **wind-vector**   Wind values, python-list length c  
 **start**         Start-position, python-list [m, n]  0 <= m < r , 0 <= n < c   
 **goal**          Target-position, python-list [p, q]  0 <= m < p , 0 <= n < q  
 **action-mode**   Valid arguments `"king"` (8-directions movement) or `"std"` (4-directions movement)

#### Utility Functions
`env.reset()`      Return to initial state for a new episode.  
`env.printenv()`   Renders the environment for visualisation.   
`state, reward, done = env.step(action)`  
Takes a step, action values ranging from 0-3  for "std" and 0-4 for "king". Returns (and updates) current position, reward obtained for taking that action and done, which is `True`, if goal is reached, `False` otherwise.
