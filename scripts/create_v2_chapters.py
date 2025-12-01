import os
import re

def create_v2_chapters():
    base_dir = r"f:\workspace_estatistica_prova"
    
    # Template for V2 Header/Top Bar
    v2_top_bar = """
    <div class="top-bar">
        <div class="top-bar-content">
            <a href="index_v2.html" class="back-btn-v2" style="text-decoration: none; display: flex; align-items: center; gap: 0.5rem; color: var(--text-primary); font-weight: 600;">
                <span>←</span> Voltar
            </a>
            
            <div class="version-badge-top">v2.0 BETA</div>

            <button id="theme-toggle" class="theme-toggle" aria-label="Alternar tema">
                <span class="theme-icon">🌙</span>
            </button>
        </div>
    </div>
    """

    for i in range(1, 11):
        filename = f"chapter{i}.html"
        v2_filename = f"chapter{i}_v2.html"
        filepath = os.path.join(base_dir, filename)
        v2_filepath = os.path.join(base_dir, v2_filename)

        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found)")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update Head
        # Add style_v2.css and overrides BEFORE chapter.css to allow overrides to work (using !important) 
        # or AFTER to cascade naturally? 
        # My overrides file uses !important for critical things.
        # Let's put them AFTER chapter.css to be safe.
        
        head_insertion = """
    <link rel="stylesheet" href="css/style_v2.css">
    <link rel="stylesheet" href="css/chapter_v2_overrides.css">
    <script src="js/app_v2.js" defer></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Mark this chapter as read
            if (window.app && window.app.progressTracker) {
                window.app.progressTracker.markAsRead(%d);
            }
        });
    </script>
        """ % i

        # Replace theme-loader with new head content
        if '<script src="js/theme-loader.js"></script>' in content:
            content = content.replace('<script src="js/theme-loader.js"></script>', head_insertion)
        else:
            # Fallback: insert before </head>
            content = content.replace('</head>', head_insertion + '\n</head>')

        # 2. Inject Top Bar at start of body
        if '<body>' in content:
            content = content.replace('<body>', '<body>\n' + v2_top_bar)

        # 3. Update Links
        content = content.replace('href="index.html"', 'href="index_v2.html"')
        
        # Regex to replace chapter links (e.g. chapter2.html -> chapter2_v2.html)
        # Be careful not to replace already replaced ones if run multiple times (though we write to new file)
        content = re.sub(r'href="chapter(\d+)\.html"', r'href="chapter\1_v2.html"', content)

        # 4. Remove/Hide V1 Nav (Handled by CSS overrides, but we can also comment it out to be cleaner)
        # content = re.sub(r'<nav class="top-nav">.*?</nav>', '', content, flags=re.DOTALL) 
        # Keeping it in DOM but hidden is safer to avoid breaking scripts that might look for it, 
        # though v2 scripts shouldn't.

        # 5. Save as v2 file
        with open(v2_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created {v2_filename}")

if __name__ == "__main__":
    create_v2_chapters()
