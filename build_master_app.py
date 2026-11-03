import json
from fiches_data import fiches_memoire
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("gen", "/home/opc/qcm-poo-java/generate.py")
gen_mod = importlib.util.module_from_spec(spec)
sys.modules["gen"] = gen_mod
spec.loader.exec_module(gen_mod)
questions = gen_mod.questions

print(f"Loaded {len(questions)} questions and {len(fiches_memoire)} fiches memoire.")

html_template = '''<!DOCTYPE html>
<html lang="fr" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QCM, Flashcards & Fiches Mémoire POO Java - ENSA Kénitra (Pr. Aniss Moumen)</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .perspective-1000 { perspective: 1000px; }
        .transform-style-3d { transform-style: preserve-3d; }
        .backface-hidden { backface-visibility: hidden; }
        .rotate-y-180 { transform: rotateY(180deg); }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-full flex flex-col justify-between antialiased">

    <!-- Header -->
    <header class="bg-slate-800 border-b border-slate-700 sticky top-0 z-50 px-4 py-3 shadow-md">
        <div class="max-w-5xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
            <div>
                <h1 class="text-base sm:text-lg font-bold text-emerald-400 flex items-center gap-2">
                    <span>☕</span> POO Java Masterclass - ENSAK
                </h1>
                <p class="text-xs text-slate-400">Pr. Aniss Moumen | QCM, Flashcards & Fiches Mémoire</p>
            </div>
            <div class="flex items-center gap-3">
                <div id="mode-toggle-container" class="bg-slate-700 p-1 rounded-xl flex gap-1 border border-slate-600">
                    <button id="mode-qcm-btn" onclick="switchMode('qcm')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition bg-emerald-500 text-slate-950 cursor-pointer">QCM</button>
                    <button id="mode-flash-btn" onclick="switchMode('flash')" class="px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer">Flashcards</button>
                    <button id="mode-fiches-btn" onclick="switchMode('fiches')" class="px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer">Fiches Mémoire</button>
                </div>
                <div id="score-badge" class="bg-slate-700 px-3 py-1 rounded-full text-xs font-semibold text-emerald-300 border border-slate-600">
                    Score: <span id="current-score">0</span>/<span id="total-questions">__TOTAL_Q__</span>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-3xl w-full mx-auto p-4 flex-grow flex flex-col justify-center">
        
        <!-- Welcome Screen -->
        <div id="welcome-screen" class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-xl text-center">
            <div class="text-4xl mb-3">🚀</div>
            <h2 class="text-xl font-bold mb-2 text-white">Règles & Maîtrise Totale POO Java (ENSAK)</h2>
            <p class="text-slate-300 text-sm mb-6 leading-relaxed">
                Ce hub de révision ultime couvre l'intégralité du cours de Pr. Aniss Moumen (105 questions QCM, 105 flashcards et des <b>Fiches Mémoire détaillées</b> pour chaque chapitre jusqu'à la hiérarchie). Choisissez votre mode !
            </p>
            <div class="flex flex-col sm:flex-row gap-3 justify-center">
                <button onclick="startMode('qcm')" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold px-5 py-3 rounded-xl transition shadow-lg cursor-pointer text-xs">
                    Mode QCM (105 Q)
                </button>
                <button onclick="startMode('flash')" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-5 py-3 rounded-xl transition shadow-lg cursor-pointer text-xs">
                    Mode Flashcards
                </button>
                <button onclick="startMode('fiches')" class="bg-amber-600 hover:bg-amber-700 text-white font-bold px-5 py-3 rounded-xl transition shadow-lg cursor-pointer text-xs">
                    Fiches Mémoire (Cours)
                </button>
            </div>
        </div>

        <!-- QCM Quiz Screen -->
        <div id="quiz-screen" class="hidden bg-slate-800 border border-slate-700 rounded-2xl p-5 sm:p-6 shadow-xl">
            <div class="mb-4 flex justify-between items-center">
                <span id="progress-text" class="text-xs text-slate-400 font-medium">Question 1 sur __TOTAL_Q__</span>
                <span id="category-badge" class="bg-emerald-900/50 text-emerald-300 px-2 py-0.5 rounded border border-emerald-700/50 text-[10px] uppercase font-semibold">Base</span>
            </div>
            <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden mb-5">
                <div id="progress-bar" class="bg-emerald-500 h-full transition-all duration-300" style="width: 0%"></div>
            </div>

            <div class="mb-5">
                <h3 id="question-title" class="text-base sm:text-lg font-semibold text-white mb-4 leading-snug"></h3>
                <div id="options-container" class="space-y-3"></div>
            </div>

            <div id="explanation-box" class="hidden mt-4 p-4 rounded-xl border text-sm transition-all">
                <h4 id="explanation-title" class="font-bold mb-1 flex items-center gap-1.5"></h4>
                <p id="explanation-text" class="text-slate-300 text-xs sm:text-sm leading-relaxed"></p>
            </div>

            <div class="mt-6 flex justify-between items-center gap-3">
                <button id="prev-btn" onclick="prevQuestion()" class="bg-slate-700 hover:bg-slate-600 text-slate-300 text-xs font-semibold px-4 py-2.5 rounded-xl transition disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer">
                    ← Précédent
                </button>
                <button id="next-btn" onclick="nextQuestion()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 text-xs font-bold px-6 py-2.5 rounded-xl transition shadow cursor-pointer hidden">
                    Suivant →
                </button>
                <button id="submit-ans-btn" onclick="submitAnswer()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 text-xs font-bold px-6 py-2.5 rounded-xl transition shadow cursor-pointer">
                    Valider
                </button>
            </div>
        </div>

        <!-- Flashcards Screen -->
        <div id="flashcard-screen" class="hidden flex flex-col items-center">
            <div class="w-full flex justify-between items-center mb-3 px-2">
                <span id="flash-progress" class="text-xs text-slate-400 font-medium">Carte 1 sur __TOTAL_Q__</span>
                <span id="flash-category" class="bg-indigo-900/50 text-indigo-300 px-2.5 py-0.5 rounded border border-indigo-700/50 text-[10px] uppercase font-semibold"></span>
            </div>

            <!-- Flip Card Container -->
            <div class="w-full perspective-1000 h-80 sm:h-72 cursor-pointer mb-5" onclick="flipCard()">
                <div id="flash-card-inner" class="relative w-full h-full duration-500 transform-style-3d shadow-2xl rounded-2xl">
                    <!-- Recto -->
                    <div class="absolute inset-0 w-full h-full bg-slate-800 border-2 border-slate-700 rounded-2xl p-6 flex flex-col justify-between backface-hidden">
                        <div class="text-xs text-indigo-400 font-semibold">QUESTION / NOTION (Cliquez pour retourner) 🔄</div>
                        <div class="my-auto">
                            <h3 id="flash-front" class="text-base sm:text-lg font-bold text-white text-center leading-snug"></h3>
                        </div>
                        <div class="text-center text-xs text-slate-400">Touchez la carte pour voir la réponse</div>
                    </div>
                    <!-- Verso -->
                    <div class="absolute inset-0 w-full h-full bg-slate-750 border-2 border-indigo-500/50 rounded-2xl p-6 flex flex-col justify-between backface-hidden rotate-y-180">
                        <div class="text-xs text-emerald-400 font-semibold">RÉPONSE & EXPLICATION ✨</div>
                        <div class="my-auto overflow-y-auto max-h-40">
                            <p id="flash-back" class="text-slate-200 text-xs sm:text-sm text-center leading-relaxed font-medium"></p>
                        </div>
                        <div class="text-center text-xs text-slate-400">Touchez pour revenir au recto</div>
                    </div>
                </div>
            </div>

            <!-- Flash Navigation -->
            <div class="w-full flex justify-between items-center gap-3">
                <button onclick="prevFlash()" class="bg-slate-700 hover:bg-slate-600 text-slate-300 text-xs font-semibold px-5 py-2.5 rounded-xl transition cursor-pointer">
                    ← Précédente
                </button>
                <button onclick="nextFlash()" class="bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold px-6 py-2.5 rounded-xl transition shadow cursor-pointer">
                    Suivante →
                </button>
            </div>
        </div>

        <!-- Fiches Mémoire Screen -->
        <div id="fiches-screen" class="hidden bg-slate-800 border border-slate-700 rounded-2xl p-5 sm:p-6 shadow-xl">
            <div class="flex justify-between items-center mb-4">
                <div>
                    <h3 id="fiche-title" class="text-lg font-bold text-amber-400"></h3>
                    <p id="fiche-subtitle" class="text-xs text-slate-400 mt-0.5"></p>
                </div>
                <span id="fiche-counter" class="bg-amber-900/50 text-amber-300 px-2.5 py-1 rounded border border-amber-700/50 text-xs font-semibold"></span>
            </div>
            
            <div class="bg-slate-900/70 border border-slate-700 rounded-xl p-4 sm:p-5 mb-5 max-h-96 overflow-y-auto">
                <ul id="fiche-points-list" class="space-y-3 text-xs sm:text-sm text-slate-200 leading-relaxed">
                    <!-- Points injected here -->
                </ul>
            </div>

            <div class="flex justify-between items-center">
                <button onclick="prevFiche()" class="bg-slate-700 hover:bg-slate-600 text-slate-300 text-xs font-semibold px-4 py-2.5 rounded-xl transition cursor-pointer">
                    ← Chapitre Précédent
                </button>
                <button onclick="nextFiche()" class="bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold px-5 py-2.5 rounded-xl transition shadow cursor-pointer">
                    Chapitre Suivant →
                </button>
            </div>
        </div>

        <!-- Results Screen -->
        <div id="results-screen" class="hidden bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-xl text-center">
            <div class="text-5xl mb-3" id="result-emoji">🎉</div>
            <h2 class="text-2xl font-bold mb-2 text-white">Session Terminée !</h2>
            <p id="final-score-text" class="text-lg text-emerald-400 font-semibold mb-4">Votre score : 0 / __TOTAL_Q__</p>
            <p id="result-message" class="text-slate-300 text-sm mb-6 leading-relaxed"></p>
            <div class="flex flex-col sm:flex-row gap-3 justify-center">
                <button onclick="restartQuiz()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold px-6 py-3 rounded-xl transition shadow cursor-pointer text-xs">
                    Recommencer
                </button>
                <button onclick="startMode('fiches')" class="bg-amber-600 hover:bg-amber-700 text-white font-bold px-6 py-3 rounded-xl transition shadow cursor-pointer text-xs">
                    Relire les Fiches Mémoire
                </button>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="text-center py-4 text-xs text-slate-500 border-t border-slate-800">
        QCM, Flashcards & Fiches Mémoire POO Java • ENSA Kénitra • Optimisé Mobile
    </footer>

    <script>
        const questions = __QUESTIONS_JSON__;
        const fiches = __FICHES_JSON__;

        let currentMode = 'qcm';
        let currentIndex = 0;
        let currentFicheIndex = 0;
        let score = 0;
        let selectedOption = null;
        let answered = false;
        let userAnswers = new Array(questions.length).fill(null);
        let isFlipped = false;

        const welcomeScreen = document.getElementById('welcome-screen');
        const quizScreen = document.getElementById('quiz-screen');
        const flashcardScreen = document.getElementById('flashcard-screen');
        const fichesScreen = document.getElementById('fiches-screen');
        const resultsScreen = document.getElementById('results-screen');

        function switchMode(mode) {
            currentMode = mode;
            currentIndex = 0;
            currentFicheIndex = 0;
            welcomeScreen.classList.add('hidden');
            resultsScreen.classList.add('hidden');
            
            document.getElementById('mode-qcm-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer';
            document.getElementById('mode-flash-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer';
            document.getElementById('mode-fiches-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer';

            if (mode === 'qcm') {
                quizScreen.classList.remove('hidden');
                flashcardScreen.classList.add('hidden');
                fichesScreen.classList.add('hidden');
                document.getElementById('mode-qcm-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition bg-emerald-500 text-slate-950 cursor-pointer';
                loadQuestion();
            } else if (mode === 'flash') {
                flashcardScreen.classList.remove('hidden');
                quizScreen.classList.add('hidden');
                fichesScreen.classList.add('hidden');
                document.getElementById('mode-flash-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition bg-indigo-600 text-white cursor-pointer';
                loadFlashcard();
            } else if (mode === 'fiches') {
                fichesScreen.classList.remove('hidden');
                quizScreen.classList.add('hidden');
                flashcardScreen.classList.add('hidden');
                document.getElementById('mode-fiches-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition bg-amber-600 text-white cursor-pointer';
                loadFiche();
            }
        }

        function startMode(mode) {
            switchMode(mode);
        }

        function loadQuestion() {
            const q = questions[currentIndex];
            document.getElementById('question-title').textContent = (currentIndex + 1) + '. ' + q.q;
            document.getElementById('category-badge').textContent = q.cat;
            document.getElementById('progress-text').textContent = 'Question ' + (currentIndex + 1) + ' sur ' + questions.length;
            document.getElementById('progress-bar').style.width = (((currentIndex + 1) / questions.length) * 100) + '%';
            document.getElementById('current-score').textContent = score;

            const optsContainer = document.getElementById('options-container');
            optsContainer.innerHTML = '';
            document.getElementById('explanation-box').classList.add('hidden');
            
            selectedOption = userAnswers[currentIndex];
            answered = selectedOption !== null;

            q.opts.forEach((opt, index) => {
                const btn = document.createElement('button');
                let btnClass = 'w-full text-left p-3.5 rounded-xl border text-xs sm:text-sm transition flex items-start gap-3 cursor-pointer ';
                if (userAnswers[currentIndex] === index) {
                    btnClass += 'bg-slate-700 border-emerald-500 text-white shadow';
                } else {
                    btnClass += 'bg-slate-750 border-slate-700 hover:border-slate-500 text-slate-200';
                }
                btn.className = btnClass;
                
                if (answered) {
                    btn.disabled = true;
                    if (index === q.corr) {
                        btn.className = 'w-full text-left p-3.5 rounded-xl border bg-emerald-950/60 border-emerald-500 text-emerald-200 text-xs sm:text-sm';
                    } else if (index === selectedOption && index !== q.corr) {
                        btn.className = 'w-full text-left p-3.5 rounded-xl border bg-rose-950/60 border-rose-500 text-rose-200 text-xs sm:text-sm';
                    } else {
                        btn.className = 'w-full text-left p-3.5 rounded-xl border bg-slate-800 border-slate-700 text-slate-400 text-xs sm:text-sm opacity-60';
                    }
                }

                btn.innerHTML = '<span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-slate-700 text-xs font-bold text-slate-300 flex-shrink-0">' + String.fromCharCode(65 + index) + '</span><span class="mt-0.5">' + opt + '</span>';
                
                if (!answered) {
                    btn.onclick = function() { selectOption(index); };
                }
                optsContainer.appendChild(btn);
            });

            document.getElementById('prev-btn').disabled = currentIndex === 0;

            if (answered) {
                document.getElementById('submit-ans-btn').classList.add('hidden');
                document.getElementById('next-btn').classList.remove('hidden');
                showExplanation(selectedOption === q.corr, q);
            } else {
                document.getElementById('submit-ans-btn').classList.remove('hidden');
                document.getElementById('next-btn').classList.add('hidden');
                document.getElementById('submit-ans-btn').disabled = true;
                document.getElementById('submit-ans-btn').classList.add('opacity-50');
            }
        }

        function selectOption(index) {
            selectedOption = index;
            const buttons = document.getElementById('options-container').children;
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].className = i === index 
                    ? 'w-full text-left p-3.5 rounded-xl border bg-slate-700 border-emerald-500 text-white shadow text-xs sm:text-sm flex items-start gap-3 cursor-pointer'
                    : 'w-full text-left p-3.5 rounded-xl border bg-slate-750 border-slate-700 hover:border-slate-500 text-slate-200 text-xs sm:text-sm flex items-start gap-3 cursor-pointer';
            }
            const submitBtn = document.getElementById('submit-ans-btn');
            submitBtn.disabled = false;
            submitBtn.classList.remove('opacity-50');
        }

        function submitAnswer() {
            if (selectedOption === null) return;
            answered = true;
            userAnswers[currentIndex] = selectedOption;
            if (selectedOption === questions[currentIndex].corr) {
                score++;
            }
            document.getElementById('current-score').textContent = score;
            loadQuestion();
        }

        function showExplanation(isCorrect, q) {
            const box = document.getElementById('explanation-box');
            box.classList.remove('hidden');
            if (isCorrect) {
                box.className = 'mt-4 p-4 rounded-xl border bg-emerald-950/40 border-emerald-600/50 text-emerald-200 text-sm';
                document.getElementById('explanation-title').innerHTML = '<span>✅</span> Bonne réponse !';
            } else {
                box.className = 'mt-4 p-4 rounded-xl border bg-rose-950/40 border-rose-600/50 text-rose-200 text-sm';
                document.getElementById('explanation-title').innerHTML = '<span>❌</span> Mauvaise réponse. La bonne réponse était : <b>' + String.fromCharCode(65 + q.corr) + '</b>';
            }
            document.getElementById('explanation-text').textContent = q.exp;
        }

        function nextQuestion() {
            if (currentIndex < questions.length - 1) {
                currentIndex++;
                loadQuestion();
            } else {
                showResults();
            }
        }

        function prevQuestion() {
            if (currentIndex > 0) {
                currentIndex--;
                loadQuestion();
            }
        }

        // --- Flashcard Logic ---
        function loadFlashcard() {
            const q = questions[currentIndex];
            document.getElementById('flash-progress').textContent = 'Carte ' + (currentIndex + 1) + ' sur ' + questions.length;
            document.getElementById('flash-category').textContent = q.cat;
            document.getElementById('flash-front').textContent = q.q;
            
            const correctOptText = q.opts[q.corr];
            document.getElementById('flash-back').innerHTML = '<b>Réponse :</b> ' + correctOptText + '<br><br><span class="text-xs text-slate-300">' + q.exp + '</span>';
            
            isFlipped = false;
            document.getElementById('flash-card-inner').style.transform = 'rotateY(0deg)';
        }

        function flipCard() {
            isFlipped = !isFlipped;
            const inner = document.getElementById('flash-card-inner');
            inner.style.transform = isFlipped ? 'rotateY(180deg)' : 'rotateY(0deg)';
        }

        function nextFlash() {
            if (currentIndex < questions.length - 1) {
                currentIndex++;
                loadFlashcard();
            } else {
                showResults();
            }
        }

        function prevFlash() {
            if (currentIndex > 0) {
                currentIndex--;
                loadFlashcard();
            }
        }

        // --- Fiches Mémoire Logic ---
        function loadFiche() {
            const f = fiches[currentFicheIndex];
            document.getElementById('fiche-title').textContent = f.chapitre;
            document.getElementById('fiche-subtitle').textContent = f.resume;
            document.getElementById('fiche-counter').textContent = 'Chapitre ' + (currentFicheIndex + 1) + ' / ' + fiches.length;

            const listContainer = document.getElementById('fiche-points-list');
            listContainer.innerHTML = '';
            f.points.forEach(pt => {
                const li = document.createElement('li');
                li.className = 'flex items-start gap-2 border-b border-slate-800 pb-2';
                li.innerHTML = '<span class="text-amber-400 mt-0.5">🔹</span><span>' + pt + '</span>';
                listContainer.appendChild(li);
            });
        }

        function nextFiche() {
            if (currentFicheIndex < fiches.length - 1) {
                currentFicheIndex++;
                loadFiche();
            }
        }

        function prevFiche() {
            if (currentFicheIndex > 0) {
                currentFicheIndex--;
                loadFiche();
            }
        }

        function showResults() {
            quizScreen.classList.add('hidden');
            flashcardScreen.classList.add('hidden');
            fichesScreen.classList.add('hidden');
            resultsScreen.classList.remove('hidden');
            document.getElementById('final-score-text').textContent = 'Votre score QCM : ' + score + ' / ' + questions.length;
            
            const percentage = (score / questions.length) * 100;
            const emoji = document.getElementById('result-emoji');
            const msg = document.getElementById('result-message');

            if (percentage >= 80) {
                emoji.textContent = '🏆';
                msg.textContent = 'Exceptionnel ! Vous maîtrisez parfaitement l’ensemble du cours POO Java de l’ENSA Kénitra.';
            } else if (percentage >= 50) {
                emoji.textContent = '👍';
                msg.textContent = 'Très bon niveau ! Quelques révisions en mode Flashcards ou Fiches Mémoire vous permettront d’atteindre l’excellence.';
            } else {
                emoji.textContent = '📚';
                msg.textContent = 'Consultez les Fiches Mémoire pour réviser chaque chapitre en profondeur !';
            }
        }

        function restartQuiz() {
            currentIndex = 0;
            score = 0;
            userAnswers = new Array(questions.length).fill(null);
            resultsScreen.classList.add('hidden');
            if (currentMode === 'qcm') {
                quizScreen.classList.remove('hidden');
                loadQuestion();
            } else if (currentMode === 'flash') {
                flashcardScreen.classList.remove('hidden');
                loadFlashcard();
            } else {
                fichesScreen.classList.remove('hidden');
                loadFiche();
            }
        }
    </script>
</body>
</html>
'''

final_html = html_template.replace('__TOTAL_Q__', str(len(questions))).replace('__QUESTIONS_JSON__', json.dumps(questions, ensure_ascii=False)).replace('__FICHES_JSON__', json.dumps(fiches_memoire, ensure_ascii=False))

with open('/home/opc/qcm-poo-java/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully generated index.html with QCM, Flashcards and Fiches Mémoire!")
