# Match expressions

The match expression provides branching control that is based on  
the comparison of an expression with a set of patterns.

## String constant

```F#
open System
open System.Globalization

printf "What is the capital of Slovakia?: "

let name = Console.ReadLine()
let lowered = name.ToLower()
let capital = CultureInfo.CurrentCulture.TextInfo.ToTitleCase lowered

let msg = match capital with
            | "Bratislava" -> "correct answer"
            | _ -> "wrong answer"


printfn $"{msg}"
```
