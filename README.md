# Word Puzzle Helpers

## Wordle Solver

* Python3
* Parameters
 - `-w` Supply starting word. Default is randomly-selected one from `five-letter-words.txt` (that's marked as a starter)
 - `--dictionary` newline-separated list of valid words. Defaults to `five-letter-words.txt`. This file may contain special markers.
   Starter words are prefixed with `!`, and already used words (caution: may be out of date!) are prefixed with `#` and will not be 
   offered as guesses.

This program is interactive. Flow is:
  * Program offers a guess.
  * Program prompts for the CLUE to your guess. Enter `-` for a letter that's just wrong. Enter a lower-case for a letter that's right
    but in the wrong place. Enter an upper-case letter that's in the right place. 
    Note: Program assumes that if there are repeat letters in your guess but there is only one in the answer,
    you will enter a clue that indicates both conditions.  For example, if the answer is `alien` and you put `lolly` the clue you respond to
    the program should be `l-ll-`. Not sure what the actual Wordle behavior is, so 

## Letterbox Solver

* Python3
* Supply two parameters:
 - `--puzzle` the edges of the puzzle. Each edge is a string and the edges are separated by hyphens: e.g. `--puzzle=tlk-ons-ubi-awe`
 - `--dictionary` newline-separated list of valid words. Defaults to `words.txt`

Run the program with the parameters, and it will produce an exhaustive list of solutions. For the above example, the output is:

```
Solutions for letterbox tlk-ons-ubi-awe: 
 * antinuke-elbows
 * bailout-twinkies
 * bakelites-sunbow
 * bakelites-sunbows
 * bakelites-swoun
 * blowiest-tanuki
 * blowiest-tanukis
 * blowouts-sinkable
 * blowouts-skankiest
 * blowsiest-tanuki
 * blowsiest-tanukis
 * bowlike-eluants
 * bowlines-stakeout
 * bowlines-stakeouts
 * kaolinites-sunbow
 * kaolinites-sunbows
 * kotows-sustainable
 * kowtows-sustainable
 * lauwines-steinbok
 * lauwines-steinboks
 * outbakes-slantwise
 * outwiles-sinkable
 * outwits-sinkable
 * sunbows-slatelike
 * towboats-sinuslike
 * towboats-sunlike
 * unakite-elbows
 * unlikeliest-towboat
 * unlikeliest-towboats
 * woks-sustainable
```
