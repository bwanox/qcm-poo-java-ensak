import json

# We already have questions. Let's add Fiches Mémoire content per chapter.
fiches_memoire = [
    {
        "chapitre": "Chapitre 1 : Introduction à la POO & UML",
        "resume": "Fondements de la Programmation Orientée Objet et modélisation graphique.",
        "points": [
            "<b>Définition d'une classe :</b> Une classe est une catégorie ou un modèle d'objets partageant les mêmes attributs (données) et méthodes (fonctions). <i>UNE CLASSE = {MÉTHODES + ATTRIBUTS}</i>.",
            "<b>Évolution historique :</b> Bjarne Stroustrup a créé C++ en « greffant » les classes sur le langage C (procédural).",
            "<b>Les 4 Piliers de la POO :</b>",
            "1. <i>Encapsulation :</i> Masquage des données et passage obligé par les méthodes.",
            "2. <i>Héritage :</i> Création d'une nouvelle classe à partir d'une classe existante pour réutiliser et étendre le code.",
            "3. <i>Polymorphisme :</i> Capacité d'une classe fille à redéfinir les méthodes héritées de la classe mère.",
            "4. <i>Abstraction :</i> Modélisation simplifiée d'entités du monde réel.",
            "<b>Rôle d'UML :</b> Langage de modélisation visuel (diagrammes de classes, de séquence, etc.) pour spécifier et documenter le système."
        ]
    },
    {
        "chapitre": "Chapitre 2 : Introduction à Java & JVM",
        "resume": "Architecture, portabilité et syntaxe de démarrage de la machine virtuelle Java.",
        "points": [
            "<b>Portabilité (\"Write Once, Run Anywhere\") :</b> Le code source `.java` est compilé en un code intermédiaire appelé <i>bytecode</i> (`.class`), exécutable sur toute machine dotée d'une JVM.",
            "<b>Composants de la JVM :</b> Le <i>Class Loader</i> (chargeur de classes) et le compilateur JIT (Just-In-Time) pour optimiser les performances à l'exécution.",
            "<b>JDK vs JRE :</b> Le JDK inclut le JRE plus les outils de développement (compilateur `javac`, etc.).",
            "<b>Méthode `main` :</b> Point d'entrée obligatoire : `public static void main(String[] args)`.",
            "<b>Flux d'E/S :</b> `System.out.println()` (flux de sortie standard) et la classe `Scanner` du package `java.util` pour lire les entrées clavier."
        ]
    },
    {
        "chapitre": "Chapitre 3 : Classes & Objets",
        "resume": "Variables, types enveloppants et instanciation en mémoire.",
        "points": [
            "<b>Variable d'instance vs Variable de classe (`static`) :</b>",
            "- <i>Variable d'instance :</i> Chaque objet possède sa propre copie de l'attribut.",
            "- <i>Variable de classe (`static`) :</i> Unique et partagée entre toutes les instances de la classe.",
            "<b>Classes Enveloppantes (Wrappers) :</b> `Integer`, `Double`, `Character`, `Boolean`, etc. Enveloppent les types primitifs pour les utiliser dans les collections.",
            "<b>Instanciation :</b> `NomClasse obj = new NomClasse();` crée l'objet dans le tas (heap) et retourne sa référence.",
            "<b>Valeur `null` :</b> Une référence d'objet non initialisée vaut `null`. Toute tentative d'accès lève une `NullPointerException`."
        ],
        "chapitre": "Chapitre 4 : Méthodes, Surcharge, `this` & Récursivité",
        "resume": "Signatures, passage de paramètres et portée.",
        "points": [
            "<b>Transmission des arguments :</b> Toujours <b>par valeur</b> en Java (copie de la valeur primitive ou copie de la référence de l'objet).",
            "<b>Surcharge (Overloading) :</b> Plusieurs méthodes portant le <i>même nom</i> dans la même classe mais ayant des signatures différentes (paramètres différents). Le type de retour seul ne suffit pas.",
            "<b>Mot-clé `this` :</b> Référence implicite désignant l'instance courante de la classe.",
            "<b>Méthodes statiques :</b> Appelables via `NomClasse.methode()` sans instanciation. Ne peuvent pas accéder directement aux membres d'instance (pas de `this`).",
            "<b>Récursivité :</b> Méthode s'appelant elle-même avec impérativement un cas de base pour éviter le `StackOverflowError`."
        ]
    },
    {
        "chapitre": "Chapitre 5 : Encapsulation, Visibilité & Packages",
        "resume": "Contrôle d'accès, encapsulation et espaces de noms.",
        "points": [
            "<b>Niveaux de visibilité :</b>",
            "1. `private` : Accessible uniquement dans la classe d'origine.",
            "2. <i>Par défaut (package-private) :</i> Accessible dans tout le même package.",
            "3. `protected` : Accessible dans le package et les sous-classes.",
            "4. `public` : Accessible partout.",
            "<b>Encapsulation pratique :</b> Attributs en `private` + méthodes d'accès publiques (`getters` et `setters`).",
            "<b>Packages & Import :</b> `package mon.paquetage;` en première ligne. `import` pour éviter les noms qualifiés complets."
        ]
    },
    {
        "chapitre": "Chapitre 6 : Constructeurs & Gestion mémoire",
        "resume": "Initialisation des objets et Garbage Collector.",
        "points": [
            "<b>Constructeur :</b> Méthode portant le nom exact de la classe, sans type de retour, appelée avec `new`.",
            "<b>Types de constructeurs :</b> Par défaut (sans argument), avec arguments, et par copie (clonage d'un objet existant).",
            "<b>Chaining (`this(...)`) :</b> Appel d'un constructeur par un autre au sein de la même classe (doit être la 1ère instruction).",
            "<b>Garbage Collector :</b> Nettoyeur automatique de la JVM qui libère la mémoire des objets non référencés dans le tas.",
            "<b>Pas de destructeur explicite :</b> Contrairement au C++ (`~NomClasse`), Java gère la destruction automatiquement."
        ]
    },
    {
        "chapitre": "Chapitre 7 : Hiérarchie, Héritage, Polymorphisme & `final`",
        "resume": "Extension de classes, polymorphisme et classes abstraites.",
        "points": [
            "<b>Héritage (`extends`) :</b> Une classe fille hérite des membres non privés d'une classe mère. Héritage <i>simple</i> uniquement en Java.",
            "<b>Super-classe `Object` :</b> Super-classe universelle de toutes les classes. Fournit `toString()` et `equals()`.",
            "<b>Mot-clé `super` :</b> Permet d'appeler le constructeur de la mère (`super(...)`) ou ses membres (`super.methode()`).",
            "<b>Ordre de construction :</b> Le constructeur de la classe mère s'exécute <b>toujours avant</b> celui de la classe fille.",
            "<b>Redéfinition (`@Override`) :</b> Remplacement d'une méthode héritée en conservant la même signature.",
            "<b>Polymorphisme :</b> Utilisation d'une référence mère pour pointer vers un objet fille, avec exécution dynamique de la méthode réelle.",
            "<b>Éléments finis (`final`) :</b> Variable = constante ; Méthode = non redéfinissable ; Classe = non dérivable.",
            "<b>Classes Abstraites & Interfaces :</b> Modèles non instanciables. Une interface impose un contrat pur et permet l'implémentation multiple."
        ]
    }
]

print("Fiches memoire prepared")
