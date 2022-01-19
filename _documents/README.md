# Overview
TBD

# Lifedrain
Drain the life force from a prisoner, prolonging your life

### Interaction with prisoner
<img src="screenshots/prisoner-interaction-without-traits.PNG"/>

### Popup from lifedrain
<img src="screenshots/lifedrain-popup.PNG"/>

### Lifedrain modifier (stackable)
Each effect is one instance of it. So in this case, the effect shown is applied 3 times: 

- Fertilty: +15%
- Health: Medium Boost x3
- Life Expectancy: +15

<img src="screenshots/lifedrain-modifier.PNG"/>

# Trait drain
Drain a trait from a prisoner, making you stronger

### Interaction with prisoner that has multiple positive traits
Only the available ones are shown. 

- If you don't have the trait, you will gain it. 
- If you have a lower ranking one (eg. quick), you will gain 1 level higher (intelligent)
- TODO: Make this be a chance, and the better the trait, the higher the chance. Currently it just happens 100% of the time

<img src="screenshots/prisoner-interaction-with-traits.png"/>

### Popup when draining a particular positive trait
You can only choose one trait to be drained at a time.

<img src="screenshots/trait-drain.png"/>

# Probablity of getting traits
The probability of getting traits will be based on a learning challenge between the player and the target. 

The chance of success should be as follows

> base_chance + player_trait_level_negative_modifier + target_trait_level_postive_modifer + difference_in_learrning_modifier

The base chance and player/target trait levels can be visualised as follows:
<img src="trait-base-probability-table.png"/>
