open System

type User =
    { FirstName: string
      LastName: string
      Salary: int }

let users = [
    
        { FirstName="Robert"; LastName="Novak"; Salary=1770 };
        { FirstName="John"; LastName="Doe";  Salary=1230 };
        { FirstName="Lucy"; LastName="Novak";  Salary=670 };
        { FirstName="Ben"; LastName="Walter";  Salary=2050 };
        { FirstName="Robin"; LastName="Brown";  Salary=2300 };
        { FirstName="Amy"; LastName="Doe";  Salary=1250 };
        { FirstName="Joe"; LastName="Draker";  Salary=1190 };
        { FirstName="Janet"; LastName="Doe";  Salary=980 };
        { FirstName="Peter"; LastName="Novak";  Salary=990 };
        { FirstName="Albert"; LastName="Novak";  Salary=1930 }
]

let avg = users |> List.averageBy (fun user -> float user.Salary)
let users2 = users |> List.filter (fun user -> user.Salary > int avg)

users2 |> List.iter Console.WriteLine
