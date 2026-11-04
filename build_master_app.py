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
                    <button id="mode-qcm-btn" onclick="switchMode('qcm')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition bg-emerald-500 text-slate-950 cursor-pointer">QCM (Flux)</button>
                    <button id="mode-flash-btn" onclick="switchMode('flash')" class="px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer">Flashcards (Flux)</button>
                    <button id="mode-fiches-btn" onclick="switchMode('fiches')" class="px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer">Fiches Mémoire</button>
                </div>
                <div id="score-badge" class="bg-slate-700 px-3 py-1 rounded-full text-xs font-semibold text-emerald-300 border border-slate-600">
                    Score QCM: <span id="current-score">0</span>/<span id="total-questions">__TOTAL_Q__</span>
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
                Ce hub de révision ultime couvre l'intégralité du cours de Pr. Aniss Moumen en <b>flux déroulant continu</b> (105 questions QCM, 105 flashcards et des <b>Fiches Mémoire détaillées</b>). Choisissez votre mode !
            </p>
            <div class="flex flex-col sm:flex-row gap-3 justify-center">
                <button onclick="startMode('qcm')" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold px-5 py-3 rounded-xl transition shadow-lg cursor-pointer text-xs">
                    Mode QCM (Flux Déroulant)
                </button>
                <button onclick="startMode('flash')" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-5 py-3 rounded-xl transition shadow-lg cursor-pointer text-xs">
                    Flashcards (Flux Déroulant)
                </button>
                <button onclick="startMode('fiches')" class="bg-amber-600 hover:bg-amber-700 text-white font-bold px-5 py-3 rounded-xl transition shadow-lg cursor-pointer text-xs">
                    Fiches Mémoire (Cours)
                </button>
            </div>
        </div>

        <!-- QCM Scrolling Screen -->
        <div id="quiz-screen" class="hidden flex flex-col w-full">
            <div class="mb-4 text-center">
                <h3 class="text-lg font-bold text-emerald-400">📝 QCM - Flux Déroulant (105 Questions)</h3>
                <p class="text-xs text-slate-400">Répondez à votre rythme, vérifiez instantanément vos réponses et suivez votre score en direct !</p>
            </div>
            <div id="qcm-feed" class="space-y-6 w-full pb-10">
                <!-- All QCM questions injected here -->
            </div>
        </div>

        <!-- Flashcards Scrolling Screen -->
        <div id="flashcard-screen" class="hidden flex flex-col w-full">
            <div class="mb-4 text-center">
                <h3 class="text-lg font-bold text-indigo-400">⚡ Flashcards - Flux Déroulant (105 Cartes)</h3>
                <p class="text-xs text-slate-400">Cliquez sur n'importe quelle carte pour la retourner et voir l'explication.</p>
            </div>
            <div id="flashcards-feed" class="space-y-4 w-full pb-10">
                <!-- All flashcards injected here -->
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

    </main>

    <!-- Footer -->
    <footer class="text-center py-4 text-xs text-slate-500 border-t border-slate-800">
        QCM, Flashcards & Fiches Mémoire POO Java • ENSA Kénitra • Optimisé Mobile
    </footer>

    <script>
        const questions = __QUESTIONS_JSON__;
        const fiches = __FICHES_JSON__;

        let currentMode = 'qcm';
        let currentFicheIndex = 0;
        let score = 0;
        let userAnswers = {}; // questionIndex -> selectedOptionIndex
        let checkedQuestions = {}; // questionIndex -> boolean

        const welcomeScreen = document.getElementById('welcome-screen');
        const quizScreen = document.getElementById('quiz-screen');
        const flashcardScreen = document.getElementById('flashcard-screen');
        const fichesScreen = document.getElementById('fiches-screen');

        function switchMode(mode) {
            currentMode = mode;
            currentFicheIndex = 0;
            welcomeScreen.classList.add('hidden');
            
            document.getElementById('mode-qcm-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer';
            document.getElementById('mode-flash-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer';
            document.getElementById('mode-fiches-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-semibold transition text-slate-300 hover:text-white cursor-pointer';

            if (mode === 'qcm') {
                quizScreen.classList.remove('hidden');
                flashcardScreen.classList.add('hidden');
                fichesScreen.classList.add('hidden');
                document.getElementById('mode-qcm-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition bg-emerald-500 text-slate-950 cursor-pointer';
                renderQCMFeed();
            } else if (mode === 'flash') {
                flashcardScreen.classList.remove('hidden');
                quizScreen.classList.add('hidden');
                fichesScreen.classList.add('hidden');
                document.getElementById('mode-flash-btn').className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition bg-indigo-600 text-white cursor-pointer';
                renderFlashcardsFeed();
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

        // --- QCM Feed Logic ---
        function renderQCMFeed() {
            const feed = document.getElementById('qcm-feed');
            feed.innerHTML = '';
            score = 0;
            document.getElementById('current-score').textContent = score;

            questions.forEach((q, idx) => {
                const card = document.createElement('div');
                card.className = 'bg-slate-800 border border-slate-700 rounded-xl p-4 shadow space-y-3';
                card.id = 'qcard-' + idx;

                let optsHtml = '';
                q.opts.forEach((opt, oIdx) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    optsHtml += (
                        '<button onclick="selectQCMOption(' + idx + ', ' + oIdx + ')" id="q' + idx + '-opt' + oIdx + '" class="w-full text-left p-3 rounded-lg border border-slate-700 bg-slate-750 hover:border-slate-500 text-xs sm:text-sm text-slate-200 transition flex items-start gap-2.5 cursor-pointer">' +
                            '<span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-slate-700 text-[10px] font-bold text-slate-300 flex-shrink-0">' + letter + '</span>' +
                            '<span class="mt-0.5">' + opt + '</span>' +
                        '</button>'
                    );
                });

                card.innerHTML = (
                    '<div class="flex justify-between items-center">' +
                        '<span class="text-[10px] bg-emerald-900/50 text-emerald-300 px-2 py-0.5 rounded border border-emerald-700/50 uppercase font-semibold">' + q.cat + '</span>' +
                        '<span class="text-xs text-slate-400 font-semibold">Question #' + (idx + 1) + '</span>' +
                    '</div>' +
                    '<h4 class="text-sm font-bold text-white">' + q.q + '</h4>' +
                    '<div class="space-y-2 mt-2">' + optsHtml + '</div>' +
                    '<div class="flex justify-between items-center mt-3 pt-2 border-t border-slate-700">' +
                        '<button onclick="checkQCMQuestion(' + idx + ')" id="check-btn-' + idx + '" class="bg-emerald-600 hover:bg-emerald-700 text-slate-950 font-bold px-4 py-1.5 rounded-lg text-xs transition cursor-pointer">Vérifier</button>' +
                        '<span id="qcm-feedback-' + idx + '" class="text-xs font-semibold"></span>' +
                    '</div>' +
                    '<div id="qcm-expl-' + idx + '" class="hidden mt-2 p-3 rounded-lg border text-xs"></div>'
                );
                feed.appendChild(card);
            });
        }

        function selectQCMOption(qIdx, oIdx) {
            if (checkedQuestions[qIdx]) return;
            userAnswers[qIdx] = oIdx;
            
            const q = questions[qIdx];
            q.opts.forEach((_, i) => {
                const btn = document.getElementById('q' + qIdx + '-opt' + i);
                if (i === oIdx) {
                    btn.className = 'w-full text-left p-3 rounded-lg border bg-slate-700 border-emerald-500 text-white text-xs sm:text-sm shadow flex items-start gap-2.5 cursor-pointer';
                } else {
                    btn.className = 'w-full text-left p-3 rounded-lg border border-slate-700 bg-slate-750 hover:border-slate-500 text-xs sm:text-sm text-slate-200 transition flex items-start gap-2.5 cursor-pointer';
                }
            });
        }

        function checkQCMQuestion(qIdx) {
            const selected = userAnswers[qIdx];
            if (selected === undefined || selected === null) {
                alert('Veuillez sélectionner une option d\'abord !');
                return;
            }

            checkedQuestions[qIdx] = true;
            const q = questions[qIdx];
            const isCorrect = selected === q.corr;
            
            if (isCorrect) {
                score++;
                document.getElementById('current-score').textContent = score;
            }

            q.opts.forEach((_, i) => {
                const btn = document.getElementById('q' + qIdx + '-opt' + i);
                btn.disabled = true;
                if (i === q.corr) {
                    btn.className = 'w-full text-left p-3 rounded-lg border bg-emerald-950/70 border-emerald-500 text-emerald-200 text-xs sm:text-sm';
                } else if (i === selected && !isCorrect) {
                    btn.className = 'w-full text-left p-3 rounded-lg border bg-rose-950/70 border-rose-500 text-rose-200 text-xs sm:text-sm';
                } else {
                    btn.className = 'w-full text-left p-3 rounded-lg border bg-slate-800 border-slate-700 text-slate-500 text-xs sm:text-sm opacity-50';
                }
            });

            document.getElementById('check-btn-' + qIdx).classList.add('hidden');
            const feedback = document.getElementById('qcm-feedback-' + qIdx);
            feedback.textContent = isCorrect ? '✅ Correct !' : '❌ Incorrect.';
            feedback.className = isCorrect ? 'text-xs font-bold text-emerald-400' : 'text-xs font-bold text-rose-400';

            const explBox = document.getElementById('qcm-expl-' + qIdx);
            explBox.classList.remove('hidden');
            explBox.className = isCorrect 
                ? 'mt-2 p-3 rounded-lg border bg-emerald-950/40 border-emerald-600/50 text-emerald-200 text-xs' 
                : 'mt-2 p-3 rounded-lg border bg-rose-950/40 border-rose-600/50 text-rose-200 text-xs';
            explBox.innerHTML = '<b>Explication :</b> ' + q.exp;
        }

        // --- Flashcards Feed Logic ---
        function renderFlashcardsFeed() {
            const feed = document.getElementById('flashcards-feed');
            feed.innerHTML = '';
            questions.forEach((q, idx) => {
                const card = document.createElement('div');
                card.className = 'bg-slate-800 border border-slate-700 rounded-xl p-4 shadow cursor-pointer transition hover:border-indigo-500';
                card.dataset.flipped = 'false';

                const correctText = q.opts[q.corr];

                card.innerHTML = (
                    '<div class="flex justify-between items-center mb-2">' +
                        '<span class="text-[10px] bg-indigo-900/50 text-indigo-300 px-2 py-0.5 rounded border border-indigo-700/50 uppercase font-semibold">' + q.cat + '</span>' +
                        '<span class="text-xs text-slate-400 font-semibold">Carte #' + (idx + 1) + '</span>' +
                    '</div>' +
                    '<h4 class="text-sm font-bold text-white mb-2">' + q.q + '</h4>' +
                    '<div class="answer-section hidden mt-3 pt-3 border-t border-slate-700 text-xs sm:text-sm">' +
                        '<p class="text-emerald-400 font-semibold mb-1">Réponse : ' + correctText + '</p>' +
                        '<p class="text-slate-300 leading-relaxed">' + q.exp + '</p>' +
                    '</div>' +
                    '<div class="text-[10px] text-indigo-400 font-medium text-right mt-2 flip-hint">Cliquez pour voir la réponse 🔄</div>'
                );

                card.onclick = function() {
                    const ansSec = card.querySelector('.answer-section');
                    const hint = card.querySelector('.flip-hint');
                    const isFlipped = card.dataset.flipped === 'true';
                    if (isFlipped) {
                        ansSec.classList.add('hidden');
                        hint.textContent = 'Cliquez pour voir la réponse 🔄';
                        card.dataset.flipped = 'false';
                        card.className = 'bg-slate-800 border border-slate-700 rounded-xl p-4 shadow cursor-pointer transition hover:border-indigo-500';
                    } else {
                        ansSec.classList.remove('hidden');
                        hint.textContent = 'Cliquez pour masquer 🔄';
                        card.dataset.flipped = 'true';
                        card.className = 'bg-slate-800 border-2 border-indigo-500 rounded-xl p-4 shadow-lg cursor-pointer transition';
                    }
                };

                feed.appendChild(card);
            });
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
    </script>
</body>
</html>
'''

final_html = html_template.replace('__TOTAL_Q__', str(len(questions))).replace('__QUESTIONS_JSON__', json.dumps(questions, ensure_ascii=False)).replace('__FICHES_JSON__', json.dumps(fiches_memoire, ensure_ascii=False))

with open('/home/opc/qcm-poo-java/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully generated index.html with scrolling QCM and Flashcards feeds!")
