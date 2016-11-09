# cm-contest

This repository contains the solutions for all three problems including the unit test suites used during development.

## Structure

This solution is driven by a `Makefile`, which will run all three problem implementations with the necessary parameters, 
while printing out each input and generated output files.

Each problem has its own directory with the following structure:

```
problem-x
├── fx.py
└── test.py
```

For each problem there is an input file in the root directory named `input-x.txt`. Each solution will generate an output 
file `output-x.txt` to the root directory (the paths and names are specified by the `Makefile`).

## Parameters

Each solution implementation has exactly two arguments: 

```
python fx.py <input-file-path> <output-file-path>
```

Each script will process the given input file, and generate an output file to the given path. The provided `Makefile` 
will assign the necessary arguments if you do not want to run manually the solutions.

## Makefile commands

The provided `Makefile` has the following commands:


|Command | Meaning |
|:---------|:-------------|
| `make` | Run the whole solution suite. |
| `make run` | Same as `make`. |
| `make px` | Run problem _x_ individually. |
| `make test` | Run the whole test suite. |
| `make tx` | Run the tests for problem _x_ |


# Problem descriptions

## Problem 1

```
Bárány számlálás

Vannak emberek, akik elalvás előtt bárányokat számolnak, hogy el tudjanak aludni. Mit csinálnak a bárányok ahhoz, hogy el tudjanak aludni?

A mi bárányunk egy speciális módszert talált ki. Választ egy számot: N
Majd elkezdi kimondani a következő számsorozatot: N, 2*N, 3*N ...
Amikor kimond egy számot, akkor megnézi a benne szereplő számjegyeket és számon tartja, hogy milyen számjegyeket halott már (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
Ha mind a 10 számjegyet halotta, akkor boldog és azonnal elalszik. Például:
N = 1692. Ebben ezek a számjegyek vannak: 1, 2, 6, 9.
2*N = 3384. Most már ennyi számjegy van meg összesen: 1, 2, 3, 4, 6, 8, 9.
3*N = 5076. Most már megvan mind a tíz számjegy, aludhat.

A feladat az lenne, hogy adott N számokra határozzuk meg az utolsó számot, amit kimond a bárányunk, mielőtt elalszik.

Az input fájl első sor tartalmaz pontosan egy számot: T. T darab teszteset lesz a fájlban ezt követően.
Minden teszteset leírása a fájlban egy sorból áll, ami szintén egy darab számot tartalmaz: N.
1 ≤ T ≤ 100
0 ≤ N ≤ 200
Egy lehetséges input fájl (ami 5 tesztesetet tartalmaz):
-------------------------------------------
5
0
1
2
11
1692
-------------------------------------------
(adatellenőrzéssel nem kell foglalkozni. pontosan annyi teszteset van benne, amennyi az első sorban jelölve van és minden teszteset pontonsan 1 sort tartalmaz, minden sor pontosan egy számot tartalmaz a fájlban)

Output fájl:
Minden tesztesetre egy választ tartalmazzon a következő módon:
Teszteset #x: eredmény
Ahol 'x' az adott teszteset száma, 1-től számozva. Az 'eredmény' az a szám, amit utoljára kimondott a bárány, mielőtt elaludt volna. Abban az esetben, ha hiába számol (akár a végtelenig) a bárány, akkor sem kerül elő az összes számjegy, akkor az 'INSOMNIA'-ot kell kiirni eredményül.

A fenti input fájlra a megoldás fájl így nézne ki:
-------------------------------------------
Teszteset #1: INSOMNIA
Teszteset #2: 10
Teszteset #3: 90
Teszteset #4: 110
Teszteset #5: 5076
-------------------------------------------

Teszteset #1, 0,  2 × 0 = 0, 3 × 0 = 0, stb. Szegény bárányunk nem fog elaludni sosem.

Teszteset #2, számsor: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (kell a 10-es, mert a 0 még hiányzik). Így az utolsó szám a 10.

Teszteset #3, számsor 2, 4, 6, 8, 10 ... 88, 90, ekkor elalszik. A 90-es szám előtt minden számjegyet látott már legalább egyszer, kivétel a 9-est. Emiatt 90 a megoldás, mert ez az utoljára kimondott szám.

Teszteset #4, számsor: 11, 22, 33, 44, 55, 66, 77, 88, 99, 110 és megvan mind, elalszik a bárány. A 110 a megoldás

Teszteset #5: ez volt a fent bemutatott példa.
```

## Problem 2

```
Palacsintázás

A CM csapat felkerekedett, hogy palacsintázzon egy jót közösen, mivel az a hír járta, hogy a Bécsi vendéglőben ingyen palacsintát osztogatatnak ebédre.
A hír igaz volt, azonban az étterem csak korlátozott számú palacsintával rendelkezett. A palacsintákat a lehető leggyorsabban kellene elfogyasztania a vendégeknek (közeledik az NTAS határidő, nem érünk rá egész nap ebédelni). Találjuk ki, hogy miként lehetne ezt megtenni.

A Vendéglő éppen ezért speciális szabályokat vezetett be (mivel Gábor felügyeli a rendet, ezért ezeket a szabályokat mindenki be is tartja).
Kezdetben pontosan D darabszámú tányéron van palacsinta, minden tányéron meghatározott (P1, P2,... Pi, ...PD) darabszámú palacsinta található. Pi: az i-ik tányéron található palacsinták száma.

Az étkezde végtelen számú üres tányérral rendelkezik és mivel kígyózó sorok állnak az Üllői úton, ezért végtelen sok vevő tud még bekapcsolódni az étkezésbe.

Normális esetben minden percben minden vásárló, akinek a tányérján van palacsinta, az megeszik egy palacsintát a saját tányérjáról.
Azonban a konyhafőnök meghatározhat Speciális perceket. A Speciális percben a konyhafőnök kiválaszt egyetlen nem üres tányért. Arról a tányérról tetszőleges számú palacsintát áttehet egy másik tányérra (akár egy új vásárló teljesen üres tányérjára is). Ez a speciális művelet szintén egy percig tart. Azonban ez idő alatt senki nem eszik egyik tányérból sem, mivel az udvariatlanság lenne.
Az ebéd akkor ér véget, ha az összes palacsinta elfogyott.

A feladat minden tesztesetnél meghatározni, hogy mennyi az a legrövidebb idő, ami alatt az ebéd befejeződhet.

Az input fájl első sora tartalmaz egy T számot , ennyi darab teszteset lesz benne.
Egy teszteset leírása két sorból áll:
Az első sora tartalmazza a D-t, hogy mennyi nem üres tányér van kezdetben.
A második sora tartalamzza a Pi számokat, hogy mennyi palacsinta van az egyes tányérokon (garantáltan D darab számot tartalmaz ez a sor, space-el elválasztva egymástól).
1 ≤ T ≤ 100
1 ≤ D ≤ 6
1 ≤ Pi ≤ 9

Egy lehetséges input fájl (3 tesztesettel):
-------------------------------------------
3
1
3
4
1 2 1 2
1
4
-------------------------------------------
(adatellenőrzéssel nem kell foglalkozni. pontosan annyi teszteset van benne, amennyi az első sorban jelölve van és minden teszteset pontonsan 2 sort tartalmaz, stb)

Az output fájl-ban a válasznak minden tesztesethez így kell kinéznie:
Teszteset #x: eredmény
Ahol 'x' az adott teszteset száma, 1-től számozva. Az 'eredmény' az a legkisebb szám, amennyi perc alatt meg lehet enni a palacsintákat.
A fenti input fájlra az eredmény:
-------------------------------------------
Teszteset #1: 3
Teszteset #2: 2
Teszteset #3: 3
-------------------------------------------

Teszteset #1:
    Adott egy tányér, azon három palacsinta. Egy optimális stratégia:
    1. perc: Speciális perc. Mivel végtelen üres tányér áll rendelkezésünkre, egy üres tányérra átteszünk a három palacsintából 1-et. (két tányárunk lett 1 és 2 db palacsintával)
    2. perc, 3 perc: Normális perc, mindenki eszik 1-1 palacsintát a tányérjáról, akinek van.
    Így 3 perc alatt vége az étkezésnek.

Teszteset #2:
    Kezdetben négy tányéron van palacsinta: 1 db, 2 db, 1 db, 2 db palacsinta van a tányérokon..
    Az optimális, ha nem szakítjuk meg egyszer sem az étkezést, hanem mindkét perc normális perc. (azaz mindenki eszik a tányérjáról egy palacsintát, ha van). Így 2 perc alatt van vége az étkezésnek.

Teszteset #3:
    Kezdetben egy tányér van, 4 palacsintával.
    1. perc: Speciális perc. 2 palacsintát átteszünk egy másik tányérra, így lesz két tányárunk 2-2 palacsintával.
    2. és 3. perc: Normális perc: mindenki eszik 1-1 palacsintát mindkét percben. ÍGy 3 perc alatt fogytak el a palacsinták.

Természetesen más teszteseteknél szükség lehet több speciális percre. (bármennyi speciális perc lehet egy tesztesetnél, a lényeg, hogy minél hamarabb befejeződjön az étkezés)

```

## Problem 3

```
	Aknakereső

Gondolom mindenki játszott már a híres Aknakereső játékkal. Azért következzen egy rövid összefoglaló a játékról.

Adott egy N*M-es méretű tábla, aminek minden mezője rejte van, nem tudjuk mit tartalmaz. Ezen kívül adott X darab akna (természetesen mindegyik különböző mezőben).
Ha rákkattintunk egy mezőre, akkor meg tudjuk nézni, hogy mit tartalmaz. Ha aknát tartalmazott, akkor vége a játéknak. Ha nem, akkor megjelenik a mezőben egy szám 0 és 8 között, ami azt mutatja, hogy az adott mezővel szomszédos többi nyolc mezőn összesen mennyi bomba található. Ha a felfedett mező 0-t tartalmaz, akkor ennek a mezőnek minden szomszédját is felfedi a kattintásunk automatikusan (ha azok is tartalmaztak 0-t, akkor rekurzívan azok szomszédos mezőit is felfedi ugyanaz az egy kattintás).
Ha az összes bombát nem tartalmazó mezőt felfedtük, akkor megnyertük a játékot.

Pl, legyen ez a kezdő tábla, ahol '.'-ok jelölik az üres mezőket, '*' az aknákat, 'c' az a mező, amire rákattintunk.
*..*...**.              *..*...**.
....*.....    ---->     1112*.....
..c..*....    ---->     00012*....
........*.    ---->     00001111*.
..........              00000001..
Mivel az kiválasztott mező szomszádai között nincs bomba (0-s mező), így felfedi a szomszédos mezőket, amik további mezőket fednek fel, így kaptuk a jobb oldalt található eredményt a kattintás után (amiben maradtak még felfedetlen mezők).

Játszani egyszerűbb, mint így leírni, ugye? Most jöjjön a feladat!

Szeretnénk minél gyorsabban megnyerni egy ilyen aknakereső játékot, márpedig az "egy kattintásos" győzelemnél nincs gyorsabb.

Az input fájl első sor tartalmaz pontosan egy számot: T. T darab teszteset lesz a fájlban ezt követően.
Mindegyik teszteset leírása pontosan egy sorból áll. Ez a sor három számot tartalmaz space-el elválasztva: N M X
N (tábla sorainak száma), M (tábla oszlopainak száma), X (bombák száma)

0 ≤ X < N * M 
1 ≤ T ≤ 230.
1 ≤ N, M ≤ 5.

Egy lehetséges input fájl (5 tesztesettel):
-------------------------------------------
5
5 5 23
3 1 1
2 2 1
4 7 3
10 10 82
-------------------------------------------
(az input fájl ellenőrzéssel nem kell törődni, garantáltan annyi teszteset van benne, amennyi kell, és a 0 ≤ X < N * M mindig teljesül, a számok space-el vannak tagolva, stb.)

Azt keressük, hogy lehetséges e úgy elhelyezni az adott méretű (N*M) táblán az X db bombát, hogy egy megfelelő kattintással meg lehessen nyerni a játékot.
Minden tesztesetre a válasznak úgy kell kinéznie, hogy:
"Teszteset #x:" (ahol 'x' az adott teszteset száma, 1-től számozva)
Ha nem lehetséges, akkor a válasz: "Lehetetlen!"
Ha lehetséges, akkor válaszul egy lehetséges konfigurációt kell leírni a fent leírt példa módján, vagyis '.' jelöli az üres mezőt a konfigban, '*' a bombák helyét, 'c' pedig azt a mezőt, amire ha rányomunk, akkor megnyerjük a játékot.
A fenti input fájlra egy lehetséges válasz:

-------------------------------------------
Teszteset #1:
Lehetetlen!
Teszteset #2:
c
.
*
Teszteset #3:
Lehetetlen!
Teszteset #4:
......*
.c....*
.......
..*....
Teszteset #5:
**********
**********
**********
****....**
***.....**
***.c...**
***....***
**********
**********
**********
-------------------------------------------

```
