import os

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

GITHUB_URL = "https://github.com/jackbrayan17/Examen-Git-IABD-EYOUM"
HF_SPACE_URL = "https://huggingface.co/spaces/JackBrayan17/Examen-Git-IABD"
SCREENSHOT_1 = os.path.join(
    "deliverables", "screenshots", "screenshot_gitattributes.png"
)
SCREENSHOT_2 = os.path.join("deliverables", "screenshots", "screenshot_action.png")

ETUDIANT = "EYOUM ATOCK"
MATRICULE = "KIA-24-2M-353"
UE = "Git & GitHub"
CLASSE = "Master 2 IABD"

BLUE = HexColor("#1f4e79")
GREEN = HexColor("#2e7d32")
GREY = HexColor("#555555")

OUT = os.path.join(
    os.path.dirname(__file__),
    "deliverables",
    "EYOUM_ATOCK_KIA-24-2M-353_Git-GitHub_Master-2-IABD.pdf",
)


def draw():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = canvas.Canvas(OUT, pagesize=A4)
    W, H = A4

    # En-tete
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2 * cm, H - 2.2 * cm, "Epreuve de Git / GitHub - Livrable")
    c.setFillColor(GREY)
    c.setFont("Helvetica", 10)
    c.drawString(
        2 * cm,
        H - 2.9 * cm,
        "KEYCE Informatique & IA - Semestre 2 - Annee 2025-2026",
    )
    c.setLineWidth(1)
    c.setStrokeColor(BLUE)
    c.line(2 * cm, H - 3.2 * cm, W - 2 * cm, H - 3.2 * cm)

    # Infos etudiant
    c.setFillColor(HexColor("#000000"))
    c.setFont("Helvetica-Bold", 11)
    y = H - 4.0 * cm
    c.drawString(2 * cm, y, f"Etudiant : {ETUDIANT}")
    c.setFont("Helvetica", 11)
    c.drawString(2 * cm, y - 0.6 * cm, f"Matricule : {MATRICULE}")
    c.drawString(2 * cm, y - 1.2 * cm, f"UE : {UE} | Classe : {CLASSE}")

    # URLs
    y2 = y - 2.2 * cm
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BLUE)
    c.drawString(2 * cm, y2, "URL du depot GitHub :")
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#0b5394"))
    c.drawString(2 * cm, y2 - 0.55 * cm, GITHUB_URL)

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(GREEN)
    c.drawString(2 * cm, y2 - 1.4 * cm, "URL du Hugging Face Space :")
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#0b5394"))
    c.drawString(2 * cm, y2 - 1.95 * cm, HF_SPACE_URL)

    # Zone captures d'ecran
    box_y_top = y2 - 2.8 * cm
    box_h = 5.3 * cm
    box_w = (W - 4 * cm - 0.8 * cm) / 2

    def screenshot_box(x, title, img):
        c.setFillColor(HexColor("#000000"))
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(x, box_y_top, title)
        top = box_y_top - 0.4 * cm
        c.setStrokeColor(GREY)
        c.setLineWidth(0.8)
        c.rect(x, top - box_h, box_w, box_h)
        path = os.path.join(os.path.dirname(__file__), img)
        if os.path.exists(path):
            try:
                c.drawImage(
                    path,
                    x + 0.1 * cm,
                    top - box_h + 0.1 * cm,
                    width=box_w - 0.2 * cm,
                    height=box_h - 0.2 * cm,
                    preserveAspectRatio=True,
                    anchor="c",
                    mask="auto",
                )
                return
            except Exception:
                pass
        c.setFillColor(GREY)
        c.setFont("Helvetica-Oblique", 9)
        c.drawCentredString(x + box_w / 2, top - box_h / 2, f"[ Inserer : {img} ]")

    screenshot_box(
        2 * cm,
        "Capture 1 : fichier .gitattributes (Git LFS local)",
        SCREENSHOT_1,
    )
    screenshot_box(
        2 * cm + box_w + 0.8 * cm,
        "Capture 2 : execution GitHub Actions",
        SCREENSHOT_2,
    )

    # Pied de page
    c.setFillColor(GREY)
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(
        W / 2,
        1.5 * cm,
        "Pipeline : git push (main) -> GitHub Actions -> Hugging Face Spaces "
        "(token via GitHub Secrets HF_TOKEN)",
    )

    c.showPage()
    c.save()
    print("PDF genere :", OUT)


if __name__ == "__main__":
    draw()
