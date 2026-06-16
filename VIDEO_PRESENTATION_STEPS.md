# Plan de presentation video

1. Presenter le contexte : projet MLOps de recommandation de repas, objectif de versionner le code et les poids du modele.
2. Montrer le depot GitHub `Examen-Git-IABD-EYOUM` et expliquer les fichiers importants : `app.py`, `requirements.txt`, `.gitattributes`, `.pre-commit-config.yaml`, `.github/workflows/deploy.yml`.
3. Ouvrir `.gitattributes` et expliquer que seuls les fichiers `*.pt` sont suivis par Git LFS.
4. Dans le terminal, executer `git lfs track`, `git status`, puis expliquer que `model_weights.pt` est stocke via LFS.
5. Montrer le hook pre-commit avec `pre-commit run --all-files` et expliquer que `black` garantit le formatage.
6. Faire une petite modification dans `app.py`, puis executer `git add .`, `git commit -m "Update demo app"` et `git push`.
7. Aller dans l'onglet Actions de GitHub, ouvrir le workflow "Deploy to Hugging Face Spaces" et montrer son execution.
8. Ouvrir le Space Hugging Face `JackBrayan17/Examen-Git-IABD` et montrer que l'interface Gradio est mise a jour.
9. Conclure : le token HF est protege dans GitHub Secrets sous le nom `HF_TOKEN`, jamais dans le code.
