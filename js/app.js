document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');
    const contentSection = document.getElementById('content-section');
    const chaptersGrid = document.getElementById('chapters-grid');
    const modal = document.getElementById('chapter-modal');
    const closeModal = document.querySelector('.close-modal');
    const modalBody = document.getElementById('modal-body');

    // Scroll to content
    startBtn.addEventListener('click', () => {
        contentSection.classList.remove('hidden');
        // Small delay to allow display:block to apply before adding visible class for transition
        setTimeout(() => {
            contentSection.classList.add('visible');
            contentSection.scrollIntoView({ behavior: 'smooth' });
        }, 10);
        loadChapters();
    });

    const hideModal = () => {
        modal.classList.remove('active');
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 300);
    };

    // Close modal
    closeModal.addEventListener('click', hideModal);

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            hideModal();
        }
    });

    async function loadChapters() {
        try {
            // Fetch specific chapters 1 and 2
            const [chap1Res, chap2Res] = await Promise.all([
                fetch('src/data/chapter_1.json'),
                fetch('src/data/chapter_2.json')
            ]);

            if (!chap1Res.ok || !chap2Res.ok) throw new Error('Failed to load chapters');

            const chap1 = await chap1Res.json();
            const chap2 = await chap2Res.json();

            renderChapters([chap1, chap2]);
        } catch (error) {
            console.error('Error:', error);
            chaptersGrid.innerHTML = '<p class="error-msg">Não foi possível carregar os capítulos. Verifique se o script de extração foi executado.</p>';
        }
    }

    function renderChapters(chapters) {
        chaptersGrid.innerHTML = '';

        chapters.forEach((chapter) => {
            const card = document.createElement('div');
            card.className = 'chapter-card';
            card.innerHTML = `
                <span class="chapter-number">Capítulo ${chapter.chapter_number}</span>
                <h3 class="chapter-title">${chapter.title}</h3>
                <p class="chapter-excerpt">${chapter.summary || 'Sem resumo disponível.'}</p>
            `;

            card.addEventListener('click', () => openChapter(chapter));
            chaptersGrid.appendChild(card);
        });
    }

    function openChapter(chapter) {
        const keyPointsHtml = chapter.keyPoints && chapter.keyPoints.length > 0
            ? `<ul class="key-points-list">${chapter.keyPoints.map(p => `<li>${p}</li>`).join('')}</ul>`
            : '';

        const sectionsHtml = chapter.sections && chapter.sections.length > 0
            ? chapter.sections.map(sec => `
                <div class="content-section-block">
                    <h4>${sec.title}</h4>
                    <p>${sec.content}</p>
                </div>
            `).join('')
            : '';

        const exercisesHtml = chapter.exercises && chapter.exercises.length > 0
            ? `<div class="exercises-section">
                <h3>Exercícios Práticos</h3>
                <div class="exercises-list">
                    ${chapter.exercises.map((ex, idx) => {
                // Check if exercise is an object with question and solution
                if (typeof ex === 'object' && ex.question && ex.solution) {
                    return `
                                <div class="exercise-item">
                                    <p class="exercise-question">${ex.question}</p>
                                    <button class="show-solution-btn" onclick="toggleSolution(${chapter.chapter_number}, ${idx})">
                                        <span class="btn-icon">💡</span> Mostrar Solução
                                    </button>
                                    <div class="exercise-solution hidden" id="solution-${chapter.chapter_number}-${idx}">
                                        <div class="solution-content">
                                            <strong>Solução:</strong>
                                            <p>${ex.solution.replace(/\n/g, '<br>')}</p>
                                        </div>
                                    </div>
                                </div>
                            `;
                } else {
                    // Fallback for string exercises
                    return `<div class="exercise-item"><p class="exercise-question">${ex}</p></div>`;
                }
            }).join('')}
                </div>
               </div>`
            : '';

        const num = chapter.chapter_number;

        modalBody.innerHTML = `
            <div class="modal-header">
                <h2>${chapter.title}</h2>
            </div>
            <div class="modal-body-content">
                <div class="intro-section">
                    <p class="chapter-summary"><strong>Resumo:</strong> ${chapter.summary}</p>
                    ${chapter.introduction ? `<p class="chapter-intro">${chapter.introduction}</p>` : ''}
                </div>
                
                ${keyPointsHtml ? '<h3>Pontos Chave</h3>' + keyPointsHtml : ''}
                
                <div class="main-content">
                    ${sectionsHtml}
                </div>

                ${exercisesHtml}
                
                <div class="visual-section">
                    <h3>Visualização de Conceitos</h3>
                    <div class="images-grid">
                        <div class="image-card">
                            <img src="images/chapter_${num}/concept_visualization.png" alt="Visualização Conceitual" onerror="this.src='images/placeholder.png'">
                            <p class="img-caption">Conceito</p>
                        </div>
                        <div class="image-card">
                            <img src="images/chapter_${num}/real_world_example.png" alt="Exemplo Real" onerror="this.src='images/placeholder.png'">
                            <p class="img-caption">Aplicação Real</p>
                        </div>
                    </div>
                </div>
            </div>
        `;

        modal.classList.remove('hidden');
        // Force reflow
        void modal.offsetWidth;
        modal.classList.add('active');
    }
});

// Global function to toggle solution visibility
function toggleSolution(chapterNum, exerciseIdx) {
    const solutionDiv = document.getElementById(`solution-${chapterNum}-${exerciseIdx}`);
    const button = event.target.closest('.show-solution-btn');

    if (solutionDiv.classList.contains('hidden')) {
        solutionDiv.classList.remove('hidden');
        setTimeout(() => solutionDiv.classList.add('visible'), 10);
        button.innerHTML = '<span class="btn-icon">🔼</span> Ocultar Solução';
    } else {
        solutionDiv.classList.remove('visible');
        setTimeout(() => solutionDiv.classList.add('hidden'), 300);
        button.innerHTML = '<span class="btn-icon">💡</span> Mostrar Solução';
    }
}
