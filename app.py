import gradio as gr


def greet(name: str) -> str:
    """Return a simple demo greeting for the Gradio interface."""
    clean_name = name.strip() if name else "World"
    return f"Hello {clean_name}!"


with gr.Blocks(title="Demo MLOps - Recommandation de repas") as demo:
    gr.Markdown("# Hello World - Demo MLOps")
    gr.Markdown(
        "Interface Gradio de demonstration pour le pipeline CI/CD "
        "GitHub Actions vers Hugging Face Spaces."
    )
    name_input = gr.Textbox(label="Votre nom", placeholder="World")
    output = gr.Textbox(label="Message")
    greet_btn = gr.Button("Dire bonjour")
    greet_btn.click(fn=greet, inputs=name_input, outputs=output)


if __name__ == "__main__":
    demo.launch()
