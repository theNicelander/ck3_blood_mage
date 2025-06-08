# Explain how duels work


## Code example
```bash
duel = {
    skill = learning
    target = scope:recipient
    10 = {
        desc = "I successfully indoctrinate them into the Blood Cult"
        compare_modifier = {
            value = scope:duel_value
            multiplier = 5
        }
        scope:recipient = { set_character_f aith = faith:quintessence_faith }
    }
    30 = {
        desc = "I fail"
        temporary_negative_lifeforce_effect_major = yes
    }
}
```

## Calculation

```
My stat:        27
Their stat:     7


# Calculate difference in skill:
27 - 7 = 20

# Multiply difference by multiplier, in compare_modifier
20 * 5 = 100

# Add the base value of the block, to get the total chance of this happening
100 + 10 = 110

# Sum the total value of all blocks
110 + 30 = 140

# Calculate chance of it happening
110 / 140 = 78.5%
