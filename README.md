---
title: Examen Git IABD
emoji: ":fork_and_knife:"
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# Examen-Git-IABD-EYOUM

Projet d'industrialisation d'un modele de recommandation de repas pour l'epreuve
Git/GitHub - Master 2 IABD.

- Etudiant : EYOUM ATOCK
- Matricule : KIA-24-2M-353
- GitHub : <https://github.com/jackbrayan17/Examen-Git-IABD-EYOUM>
- Hugging Face Space : <https://huggingface.co/spaces/JackBrayan17/Examen-Git-IABD>

## Contenu

- `app.py` - interface Gradio basique "Hello World".
- `model_weights.pt` - fichier binaire fictif de plus de 15 Mo, versionne avec Git LFS.
- `.gitattributes` - configuration Git LFS qui suit uniquement les fichiers `*.pt`.
- `.pre-commit-config.yaml` - hook local `pre-commit` utilisant `black`.
- `.github/workflows/deploy.yml` - workflow GitHub Actions de deploiement vers Hugging Face Spaces.

## Execution locale

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Sous Windows PowerShell :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## Pre-commit

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Pipeline CI/CD

```text
git push (main) -> GitHub Actions -> Hugging Face Spaces
```

Le token Hugging Face doit etre stocke dans GitHub :

`Settings > Secrets and variables > Actions > New repository secret`

Nom du secret : `HF_TOKEN`

Le token n'est jamais stocke en clair dans le code.
