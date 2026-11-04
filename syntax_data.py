import json

syntax_questions = [
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que retourne la méthode `length()` appelée sur un objet de type `String` en Java ?",
        "opts": [
            "Le nombre d'octets occupés en mémoire RAM.",
            "Le nombre de caractères (la longueur) de la chaîne de caractères.",
            "L'indice du dernier caractère de la chaîne.",
            "La taille maximale autorisée par le système."
        ],
        "corr": 1,
        "exp": "En Java, la méthode `length()` de la classe `String` retourne le nombre de caractères composant la chaîne."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Quelle est la différence entre l'utilisation de l'opérateur `+` et la méthode `concat()` pour les chaînes de caractères (`String`) ?",
        "opts": [
            "Il n'y a aucune différence, les deux font exactement la même chose.",
            "L'opérateur `+` est une syntaxe simplifiée pour la concaténation (acceptant tout type d'objet), tandis que `concat()` exige un objet `String` en paramètre.",
            "La méthode `concat()` modifie la chaîne d'origine, contrairement à `+`.",
            "L'opérateur `+` est réservé aux nombres uniquement."
        ],
        "corr": 1,
        "exp": "L'opérateur `+` est très flexible et peut concaténer n'importe quel type converti en texte, tandis que `concat()` prend un `String` et retourne une nouvelle chaîne."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Pourquoi doit-on utiliser la méthode `equals()` plutôt que l'opérateur `==` pour comparer le contenu de deux objets `String` ?",
        "opts": [
            "Parce que `==` provoque systématiquement un bug de compilation.",
            "Parce que `==` compare les références mémoire (les adresses des objets) et non leur contenu textuel, alors que `equals()` compare le contenu.",
            "Parce que `equals()` est plus rapide que `==`.",
            "Il n'y a aucune différence pour les chaînes de caractères."
        ],
        "corr": 1,
        "exp": "L'opérateur `==` compare les adresses mémoire (références), tandis que `equals()` compare le contenu réel des chaînes de caractères."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que fait la méthode `substring(int beginIndex, int endIndex)` sur un objet `String` ?",
        "opts": [
            "Elle supprime les caractères entre `beginIndex` et `endIndex`.",
            "Elle extrait et retourne une sous-chaîne depuis `beginIndex` (inclus) jusqu'à `endIndex` (exclu).",
            "Elle convertit la chaîne en minuscules entre ces indices.",
            "Elle recherche un motif."
        ],
        "corr": 1,
        "exp": "`substring(begin, end)` extrait la portion de chaîne en commençant à `beginIndex` inclus jusqu'à `endIndex` exclus."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "À quoi sert la méthode `String.matches(String regex)` ?",
        "opts": [
            "À comparer deux chaînes par ordre alphabétique.",
            "À vérifier si la chaîne de caractères correspond entièrement à l'expression régulière (regex) passée en paramètre (retourne true ou false).",
            "À fusionner deux fichiers texte.",
            "À remplacer des mots-clés."
        ],
        "corr": 1,
        "exp": "`String.matches` évalue si toute la chaîne respecte le motif de l'expression régulière (regex)."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que retourne la méthode `String.split(String regex)` ?",
        "opts": [
            "Un entier représentant le nombre de coupures.",
            "Un tableau de chaînes de caractères (`String[]`) issu du découpage de la chaîne selon le séparateur/regex.",
            "Un fichier texte séparé par des virgules.",
            "Rien (`void`)."
        ],
        "corr": 1,
        "exp": "`String.split()` découpe la chaîne en fonction d'un délimiteur ou d'une expression régulière et retourne un tableau de sous-chaînes (`String[]`)."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Quelle est la différence entre `String.replaceFirst(regex, replacement)` et `String.replaceAll(regex, replacement)` ?",
        "opts": [
            "Il n'y a aucune différence.",
            "`replaceFirst` remplace uniquement la première occurrence correspondant au motif, tandis que `replaceAll` remplace toutes les occurrences correspondantes.",
            "`replaceAll` ne supporte pas les expressions régulières.",
            "`replaceFirst` modifie la chaîne en place."
        ],
        "corr": 1,
        "exp": "`replaceFirst` cible la première correspondance du regex, alors que `replaceAll` applique le remplacement à toutes les correspondances trouvées."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Comment fonctionne la méthode `System.out.printf(String format, Object... args)` par rapport à `println()` ?",
        "opts": [
            "Elle ne fonctionne qu'avec des nombres entiers.",
            "Elle permet d'afficher du texte formaté (avec des spécificateurs comme `%s`, `%d`, `%f`) sur la sortie standard, similaire au `printf` du langage C.",
            "Elle écrit les données dans un fichier binaire.",
            "Elle est obsolète en Java."
        ],
        "corr": 1,
        "exp": "`System.out.printf()` et `String.format()` permettent un formatage précis de la sortie en utilisant des formateurs de type C."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Quelle est la différence entre les méthodes `next()` et `nextLine()` de la classe `Scanner` pour la lecture clavier ?",
        "opts": [
            "`next()` lit une ligne entière incluant les espaces, tandis que `nextLine()` lit un seul mot.",
            "`next()` lit le prochain mot (token) séparé par des espaces, tandis que `nextLine()` lit toute la ligne jusqu'au saut de ligne (`\\n`).",
            "Il n'y a aucune différence.",
            "`nextLine()` ne fonctionne qu'avec des nombres."
        ],
        "corr": 1,
        "exp": "`next()` s'arrête au premier espace (mot par mot), alors que `nextLine()` consomme toute la ligne saisie jusqu'à l'appui sur Entrée."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "À quoi sert la classe utilitaire `java.util.Arrays` en Java ?",
        "opts": [
            "À créer des fenêtres graphiques.",
            "À fournir des méthodes statiques prédéfinies pour manipuler les tableaux (tri `Arrays.sort()`, recherche, remplissage, conversion en chaîne `Arrays.toString()`).",
            "À gérer les connexions réseau.",
            "À compiler le bytecode."
        ],
        "corr": 1,
        "exp": "La classe `Arrays` du package `java.util` regroupe des méthodes statiques indispensables pour trier, rechercher et afficher des tableaux."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que fait la méthode statique `Integer.parseInt(String s)` ?",
        "opts": [
            "Elle convertit un entier en chaîne de caractères.",
            "Elle convertit une chaîne de caractères représentant un nombre en un type primitif `int`.",
            "Elle arrondit un nombre décimal.",
            "Elle supprime les espaces d'une chaîne."
        ],
        "corr": 1,
        "exp": "`Integer.parseInt()` analyse une chaîne de chiffres et retourne sa valeur sous forme de type primitif `int`."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que retourne la méthode `Character.isDigit(char ch)` ?",
        "opts": [
            "Un entier représentant le chiffre.",
            "Un booléen (`true` si le caractère est un chiffre de '0' à '9', sinon `false`).",
            "Le caractère converti en majuscule.",
            "Rien."
        ],
        "corr": 1,
        "exp": "`Character.isDigit()` teste si le caractère fourni est un chiffre décimal."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Quel est le rôle de la méthode mathématique `Math.sqrt(double a)` ?",
        "opts": [
            "Calculer la puissance carrée d'un nombre.",
            "Calculer et retourner la racine carrée positive d'un nombre double.",
            "Générer un nombre aléatoire.",
            "Calculer le logarithme népérien."
        ],
        "corr": 1,
        "exp": "`Math.sqrt()` (du package `java.lang`) retourne la racine carrée de son argument."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que fait la méthode `toString()` par défaut héritée de la super-classe `Object` si elle n'est pas redéfinie ?",
        "opts": [
            "Elle retourne une chaîne vide `\"\"`.",
            "Elle retourne une représentation textuelle composée du nom de la classe suivi du caractère `@` et de l'adresse de hachage de l'objet en hexadécimal.",
            "Elle lève une exception.",
            "Elle affiche le code source de la classe."
        ],
        "corr": 1,
        "exp": "Par défaut, `Object.toString()` retourne `<NomClasse>@<HashCodeHex>`, d'où l'intérêt de la redéfinir dans nos classes."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Quel est le comportement par défaut de la méthode `equals(Object obj)` dans la classe `Object` ?",
        "opts": [
            "Elle compare le contenu des attributs des deux objets.",
            "Elle compare strictement les références mémoire des deux objets (équivalent à l'opérateur `==`).",
            "Elle retourne toujours `true`.",
            "Elle supprime l'objet."
        ],
        "corr": 1,
        "exp": "Dans `Object`, `equals()` vérifie simplement si les deux références pointent vers le même objet en mémoire (`this == obj`)."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "À quoi servent les classes `StringBuffer` ou `StringBuilder` en Java par rapport à `String` ?",
        "opts": [
            "À stocker des nombres décimaux.",
            "À manipuler des chaînes de caractères de manière <b>muable</b> (modifiables en place) et optimisée pour les concaténations répétées.",
            "À remplacer les tableaux dynamiques.",
            "À crypter les mots de passe."
        ],
        "corr": 1,
        "exp": "Les objets `String` sont immuables. `StringBuilder` et `StringBuffer` permettent de modifier les chaînes en mémoire sans recréer d'objets à chaque modification, optimisant les performances."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Quelle est la différence entre `System.out.print()` et `System.out.println()` ?",
        "opts": [
            "Il n'y a aucune différence.",
            "`print()` affiche l'argument sans saut de ligne à la fin, tandis que `println()` ajoute un saut de ligne (`\\n`) après l'affichage.",
            "`print()` s'utilise uniquement pour les fichiers.",
            "`println()` est plus rapide."
        ],
        "corr": 1,
        "exp": "`print()` maintient le curseur sur la même ligne après l'affichage, alors que `println()` saute à la ligne suivante."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que retourne la méthode `String.compareTo(String anotherString)` ?",
        "opts": [
            "Un booléen (`true` ou `false`).",
            "Un entier négatif, nul ou positif selon que la chaîne courante est lexicographiquement inférieure, égale ou supérieure à l'autre chaîne.",
            "La différence de longueur entre les deux chaînes.",
            "Le nombre de caractères communs."
        ],
        "corr": 1,
        "exp": "`compareTo()` compare deux chaînes lexicographiquement (selon l'ordre alphabétique des codes Unicode) et retourne un `int`."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Que fait la méthode `String.toUpperCase()` ?",
        "opts": [
            "Elle met uniquement la première lettre en majuscule.",
            "Elle convertit tous les caractères de la chaîne en majuscules et retourne une nouvelle chaîne.",
            "Elle supprime les minuscules.",
            "Elle convertit la chaîne en type numérique."
        ],
        "corr": 1,
        "exp": "`toUpperCase()` transforme l'ensemble des caractères alphabétiques d'une chaîne en majuscules."
    },
    {
        "cat": "Syntaxe & Méthodes Prédéfinies",
        "q": "Comment convertit-on un nombre entier `int` en une chaîne de caractères `String` en Java ?",
        "opts": [
            "En utilisant `String.valueOf(nombre)` ou `Integer.toString(nombre)` (ou `nombre + \"\"`).",
            "En faisant `(String) nombre`.",
            "En appelant `nombre.asString()`.",
            "C'est impossible."
        ],
        "corr": 0,
        "exp": "`String.valueOf()` et `Integer.toString()` sont les méthodes standards pour convertir des types primitifs en `String`."
    }
]

print(f"Loaded {len(syntax_questions)} syntax questions.")
