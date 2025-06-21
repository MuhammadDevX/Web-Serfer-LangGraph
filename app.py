import gradio as gr
from web_serfer import WebSurfer


async def setup():
    web_serfer = WebSurfer()
    await web_serfer.setup()
    return web_serfer

async def process_message(web_serfer, message, success_criteria, history):
    results = await web_serfer.run_superstep(message, success_criteria, history)
    return results, web_serfer
    
async def reset():
    new_web_serfer = WebSurfer()
    await new_web_serfer.setup()
    return "", "", None, new_web_serfer

def free_resources(web_serfer):
    print("Cleaning up")
    try:
        if web_serfer:
            web_serfer.free_resources()
    except Exception as e:
        print(f"Exception during cleanup: {e}")


with gr.Blocks(title="WebSurfer", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## WebSurfer Personal Co-Worker")
    web_serfer = gr.State(delete_callback=free_resources)
    
    with gr.Row():
        chatbot = gr.Chatbot(label="WebSurfer", height=300, type="messages")
    with gr.Group():
        with gr.Row():
            message = gr.Textbox(show_label=False, placeholder="Your request to the WebSurfer")
        with gr.Row():
            success_criteria = gr.Textbox(show_label=False, placeholder="What are your success critiera?")
    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Go!", variant="primary")
        
    ui.load(setup, [], [web_serfer])
    message.submit(process_message, [web_serfer, message, success_criteria, chatbot], [chatbot, web_serfer])
    success_criteria.submit(process_message, [web_serfer, message, success_criteria, chatbot], [chatbot, web_serfer])
    go_button.click(process_message, [web_serfer, message, success_criteria, chatbot], [chatbot, web_serfer])
    reset_button.click(reset, [], [message, success_criteria, chatbot, web_serfer])

    
ui.launch(inbrowser=True)